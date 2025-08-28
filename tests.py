from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    # 1️⃣ Проверка добавления книги и жанра по умолчанию

    def test_add_new_book_default_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        assert collector.get_book_genre("Властелин колец") == ""


    # 2️⃣ set_book_genre корректный и некорректный жанр

    @pytest.mark.parametrize(
        "genre, expected",
        [
            ("Фантастика", "Фантастика"),
            ("Неизвестный жанр", ""),  # жанр не из списка
        ]
    )
    def test_set_book_genre(self, genre, expected):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", genre)
        assert collector.get_book_genre("Книга1") == expected


    # 3️⃣ get_books_with_specific_genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Фантастика")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Фантастика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert set(books) == {"Книга2", "Книга3"}


    # 4️⃣ get_books_for_children исключает возрастные жанры

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга4")
        collector.set_book_genre("Книга4", "Ужасы")  # возрастной жанр
        collector.add_new_book("Книга5")
        collector.set_book_genre("Книга5", "Фантастика")
        children_books = collector.get_books_for_children()
        assert "Книга4" not in children_books
        assert "Книга5" in children_books


    # 5️⃣ add_book_in_favorites и удаление

    def test_add_and_delete_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга6")
        collector.add_book_in_favorites("Книга6")
        assert "Книга6" in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites("Книга6")
        assert "Книга6" not in collector.get_list_of_favorites_books()


    # 6️⃣ add_book_in_favorites дубликаты не добавляются

    def test_add_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Книга7")
        collector.add_book_in_favorites("Книга7")
        collector.add_book_in_favorites("Книга7")
        assert collector.get_list_of_favorites_books().count("Книга7") == 1


    # 7️⃣ delete_book_from_favorites для книги, которой нет

    def test_delete_nonexistent_from_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Неизвестная")
        assert collector.get_list_of_favorites_books() == []


    # 8️⃣ Проверка, что словарь книг возвращает корректный результат

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга8")
        collector.set_book_genre("Книга8", "Комедии")
        assert collector.get_books_genre() == {"Книга8": "Комедии"}


    # 9️⃣ get_books_with_specific_genre для пустого жанра

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == []


    # 🔟 Проверка, что книгу нельзя добавить дважды

    def test_add_new_book_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Книга уникальная")
        collector.add_new_book("Книга уникальная")  # пытаемся добавить повторно
        books = collector.get_books_genre()
        # проверяем, что книга добавилась только один раз
        assert list(books.keys()).count("Книга уникальная") == 1