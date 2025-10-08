


from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, id : int):
        self._id = id

    @property
    def id(self):
        return self._id

    @abstractmethod
    def save(self):
        pass