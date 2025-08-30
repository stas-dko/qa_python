from main import BooksCollector
import pytest


class TestBooksCollector:

    # --- add_new_book ---
    def test_add_new_book_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        assert "Книга1" in collector.get_books_genre()

    def test_add_new_book_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Книга уникальная")
        collector.add_new_book("Книга уникальная")
        books = collector.get_books_genre()
        assert list(books.keys()).count("Книга уникальная") == 1

    # --- set_book_genre ---
    def test_set_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Фантастика")
        assert collector.get_book_genre("Книга2") == "Фантастика"

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Неизвестный жанр")
        assert collector.get_book_genre("Книга3") == ""

    # --- get_book_genre ---
    def test_get_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга4")
        collector.set_book_genre("Книга4", "Комедии")
        assert collector.get_book_genre("Книга4") == "Комедии"

    # --- get_books_with_specific_genre ---
    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга5")
        collector.set_book_genre("Книга5", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга5"]

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre("Фантастика") == []

    # --- get_books_for_children ---
    def test_get_books_for_children_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга6")
        collector.set_book_genre("Книга6", "Фантастика")
        assert "Книга6" in collector.get_books_for_children()

    def test_get_books_for_children_excludes_age_restricted(self):
        collector = BooksCollector()
        collector.add_new_book("Книга7")
        collector.set_book_genre("Книга7", "Ужасы")
        assert "Книга7" not in collector.get_books_for_children()

    # --- add_book_in_favorites ---
    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга8")
        collector.add_book_in_favorites("Книга8")
        assert "Книга8" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Книга9")
        collector.add_book_in_favorites("Книга9")
        collector.add_book_in_favorites("Книга9")
        assert collector.get_list_of_favorites_books().count("Книга9") == 1

    # --- delete_book_from_favorites ---
    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга10")
        collector.add_book_in_favorites("Книга10")
        collector.delete_book_from_favorites("Книга10")
        assert "Книга10" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Нет такой книги")
        assert collector.get_list_of_favorites_books() == []

    # --- get_list_of_favorites_books ---
    def test_get_list_of_favorites_books_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга11")
        collector.add_book_in_favorites("Книга11")
        assert collector.get_list_of_favorites_books() == ["Книга11"]

    # --- get_books_genre ---
    def test_get_books_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book("Книга12")
        collector.set_book_genre("Книга12", "Комедии")
        assert collector.get_books_genre() == {"Книга12": "Комедии"}