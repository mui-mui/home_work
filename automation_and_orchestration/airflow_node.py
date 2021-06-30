from abc import ABC, abstractmethod


class IAirflowNode(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass