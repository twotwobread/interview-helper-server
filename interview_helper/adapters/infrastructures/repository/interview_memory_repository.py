from typing import Dict

from interview_helper.app.outbound_ports.interview_outbound_port import (
    InterviewOutboundPort,
)

from ..db_models.interview import Interview


class InterviewMemoryRepository(InterviewOutboundPort):
    def __init__(self) -> None:
        self.interviews = Dict[int, Interview]

    def get_all(self):
        return self.interviews

    def get_by_id(self, interview_id: int):
        return next(
            (
                interview
                for interview in self.interviews
                if interview.interview_id == interview_id
            ),
            None,
        )

    def create(self, interview):
        self.interviews.append(interview)
        return interview.interview_id

    def update(self, interview):
        for i, _interview in enumerate(self.interviews):
            if _interview.interview_id == interview.interview_id:
                self.interviews[i] = interview
                return True
        return False

    def delete(self, interview_id: int):
        for i, interview in enumerate(self.interviews):
            if interview.interview_id == interview_id:
                del self.interviews[i]
                return True
        return False
