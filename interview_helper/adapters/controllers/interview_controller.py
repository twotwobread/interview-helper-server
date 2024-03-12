from fastapi.routing import APIRouter

from ..inbound_ports.interview_inbound_port import InterviewInboundPort
from .requests.interview_request import InterviewRequestDTO
from .responses.interview_response import (
    CreateInterviewResponseDTO,
    InterviewResponseDTO,
)

router = APIRouter(prefix="/interviews")
interview_service = InterviewInboundPort()


@router.get
async def get_interviews():
    interviews = interview_service.get_all()
    return InterviewResponseDTO.from_interviews(interviews)


@router.get("/{interview_id}")
async def get_interview(interview_id: int):
    interview = interview_service.get_by_id(interview_id)
    return InterviewResponseDTO.from_entity(interview)


@router.post
async def create_interview(request: InterviewRequestDTO):
    interview_id = interview_service.create(InterviewRequestDTO.to_entity(request))
    return CreateInterviewResponseDTO(interview_id=interview_id)
