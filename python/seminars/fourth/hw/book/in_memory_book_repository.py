from seminars.fourth.hw.book.book import Book
from seminars.fourth.hw.book.book_repository import BookRepository


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._books = {str(i): Book(pk=str(i), title=f"Book{i}", author=f"Author{i}") for i in range(1, 4)}

    def find_by_pk(self, pk: str) -> Book:
        return self._books.get(pk)

    def find_all(self) -> list[Book]:
        return list(self._books.values())
