from seminars.fourth.hw.book.book import Book
from seminars.fourth.hw.book.book_repository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def find_by_pk(self, pk: str) -> Book:
        return self._book_repository.find_by_pk(pk)

    def find_all(self) -> list[Book]:
        return self._book_repository.find_all()
