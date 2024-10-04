from abc import ABC, abstractmethod, abstractclassmethod
from typing import Any


class BaseResource(ABC):

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def get_by_key(self, key: int) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def get_all_by_field(self, field: str, value: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def insert(self, data: Any) -> Any:
        raise NotImplementedError()

