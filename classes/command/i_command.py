from abc import ABC, abstractmethod


class ICommand(ABC):
    """command class for command pattern"""
    @abstractmethod
    def execute(self):
        pass
