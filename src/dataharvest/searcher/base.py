from abc import ABC, abstractmethod

from dataharvest.schema import SearchResult


class BaseSearcher(ABC):
    @abstractmethod
    def search(self, keyword: str) -> SearchResult:
        raise NotImplementedError