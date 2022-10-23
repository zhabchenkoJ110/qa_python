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

    def test_add_new_book_add_the_same_book_added_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем два раза одну и ту же книгу
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        # проверяем, что добавилась одна книга
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_for_book_which_not_in_list_none(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение')
        #добавляем рейтинг книге, которой нет в списке
        collector.set_book_rating('Преступление и наказание', 5)

        #проверяем, что у книги, которой нет в списке нет рейтинга
        assert collector.set_book_rating('Преступление и наказание', 5) == None

    def test_set_book_rating_less_one_rating_not_changed(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение')
        # добавляем рейтинг книге меньше 1
        collector.set_book_rating('Гордость и предубеждение', 0)

        # проверяем, что у книги рейтинг не изменился
        assert collector.get_book_rating('Гордость и предубеждение') == 1
    def test_set_book_rating_more_ten_rating_not_changed(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение')
        # добавляем рейтинг книге больше 10
        collector.set_book_rating('Гордость и предубеждение', 11)

        # проверяем, что у книги рейтинг не изменился
        assert collector.get_book_rating('Гордость и предубеждение') == 1

    def test_get_book_rating_book_not_in_list_none(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение')

        # проверяем, что у книги, которой нет в списке нет рейтинга
        assert collector.get_book_rating('Война и мир') == None
    def test_add_book_in_favorites_add_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги в список
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем одну книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # проверяем, что в избранное добавилась 1 кнгиа
        # список favorites, который нам возвращает метод get_list_of_favorites_books, имеет длину 1
        assert len(collector.get_list_of_favorites_books()) == 1
    def test_add_book_in_favorites_add_book_not_in_dict_books_reiting_empty_list(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги в список
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем одну книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение')

        # проверяем, что в избранное книга, которой нет в словаре books_rating, не добавилась
        # список favorites, который нам возвращает метод get_list_of_favorites_books, имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_deleted_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу в список
        collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем одну книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        #проверям, что книга добавилась в Избранное
        len(collector.get_list_of_favorites_books()) == 1
        #удаляем книгу из Избранного
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # список favorites, который нам возвращает метод get_list_of_favorites_books, имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0