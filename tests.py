from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_get_book_rating_add_new_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')
        collector.add_new_book('Колобок')

        assert len(collector.get_books_rating()) == 1

    def test_get_book_rating_add_new_book_rating_one(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')

        assert collector.get_book_rating('Колобок') == 1

    def test_add_new_book_rating_not_exist(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')

        assert collector.books_rating['Колобок'] != None

    def test_set_book_rating_change_rating_seven(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.set_book_rating('Простоквашино', 7)

        assert collector.get_book_rating('Простоквашино') == 7

    def test_get_books_with_specific_rating_rating_seven_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.set_book_rating('Простоквашино', 7)
        collector.add_new_book('Колобок')
        collector.set_book_rating('Колобок', 7)
        collector.add_new_book('Снегурочка')
        collector.set_book_rating('Снегурочка', 4)

        assert len(collector.get_books_with_specific_rating(7)) == 2

    def test_add_book_in_favorites_add_one_book_in_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.add_book_in_favorites('Простоквашино')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_book_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.add_book_in_favorites('Простоквашино')

        assert 'Простоквашино' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book_book_not_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.add_book_in_favorites('Простоквашино')
        collector.delete_book_from_favorites('Простоквашино')

        assert 'Простоквашино' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_all_books_in_favorites_in_favorites_and_in_rating_same_books(self):
        collector = BooksCollector()

        collector.add_new_book('Простоквашино')
        collector.add_book_in_favorites('Простоквашино')
        collector.add_new_book('Морозко')
        collector.add_book_in_favorites('Морозко')

        assert collector.get_list_of_favorites_books() == list(collector.get_books_rating().keys())
