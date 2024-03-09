from fastapi.routing import APIRouter

from interview_helper.adapters.responses import InterviewResponse
from interview_helper.adapters.requests import InterviewRequest
from interview_helper.app.ports.interview_inbound_port import InterviewInboundPort

router = APIRouter()
interview_service = InterviewInboundPort()


@router.get("/interviews")
async def get_interviews():
    interviews = interview_service.get_all()
    return InterviewResponse.from_list(interviews)


@router.get("/interviews/{interview_id}")
async def get_interview(interview_id: int):
    interview = interview_service.get_by_id(interview_id)
    return InterviewResponse.from(interview)


@router.post("/interviews")
async def create_interview(request: InterviewRequest):
    interview_id = interview_service.create(InterviewRequest.to_entity(request))
    return InterviewResponse.from_id(interview_id)
