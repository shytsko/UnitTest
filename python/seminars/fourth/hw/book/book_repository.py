from abc import ABC, abstractmethod

from seminars.fourth.hw.book.book import Book


class BookRepository(ABC):
    @abstractmethod
    def find_by_pk(self, pk: str) -> Book:
        pass

    @abstractmethod
    def find_all(self) -> list[Book]:
        pass
