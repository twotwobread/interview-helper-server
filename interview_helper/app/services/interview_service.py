from interview_helper.adapters.inbound_ports.interview_inbound_port import (
    InterviewInboundPort,
)

from ..outbound_ports.interview_outbound_port import InterviewOutboundPort


class InterviewService(InterviewInboundPort):
    def __init__(self, interview_outbound_port: InterviewOutboundPort) -> None:
        self.interview_outbound_port = interview_outbound_port

    def get_all(self):
        return self.interview_outbound_port.get_all()

    def get_by_id(self, interview_id: int):
        return self.interview_outbound_port.get_by_id(interview_id)

    def create(self, interview):
        return self.interview_outbound_port.create(interview)

    def update(self, interview):
        return self.interview_outbound_port.update(interview)

    def delete(self, interview_id: int):
        return self.interview_outbound_port.delete(interview_id)
