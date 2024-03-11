from abc import ABC, abstractmethod


class InterviewOutboundPort(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, interview_id: int):
        pass

    @abstractmethod
    def create(self, interview):
        pass

    @abstractmethod
    def update(self, interview):
        pass

    @abstractmethod
    def delete(self, interview_id: int):
        pass
