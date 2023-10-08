# У вас есть класс BookService, который использует интерфейс BookRepository для получения
# информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
# Mockito для создания мок-объекта BookRepository
import pytest
from mockito import mock, when

from seminars.fourth.hw.book.book import Book
from seminars.fourth.hw.book.book_repository import BookRepository
from seminars.fourth.hw.book.book_service import BookService


class TestBookService:
    @pytest.fixture(scope='class')
    def books_list(self):
        return [Book(pk=str(i), title=f"Book{i}", author=f"Author{i}") for i in range(1, 4)]

    @pytest.fixture(scope='class')
    def mock_book_repository(self, books_list):
        mock_repository = mock(BookRepository)
        when(mock_repository).find_by_pk(...).thenReturn()
        for book in books_list:
            when(mock_repository).find_by_pk(book.pk).thenReturn(book)
        when(mock_repository).find_all().thenReturn(books_list)
        return mock_repository

    def test_find_existing_book(self, books_list, mock_book_repository):
        book_service = BookService(mock_book_repository)
        book = book_service.find_by_pk("2")
        assert book == books_list[1]

    def test_find_not_existing_book(self, books_list, mock_book_repository):
        book_service = BookService(mock_book_repository)
        book = book_service.find_by_pk("5")
        assert book is None

    def test_find_all(self, books_list, mock_book_repository):
        book_service = BookService(mock_book_repository)
        books = book_service.find_all()
        assert books == books_list
