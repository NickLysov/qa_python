from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_change_rating_input_lower_rating_than_can(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_rating(name, -1)
        assert collector.get_book_rating(name) == 1

    def test_set_book_rating_change_rating_input_higher_rating_than_can(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_rating(name, 11)
        assert collector.get_book_rating(name) == 1
    def test_get_books_rating_not_added_book_has_not_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение и зомби') is None

    def test_add_book_in_favorites_cant_add_book_when_not_in_book_rating_list(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        assert collector.add_book_in_favorites(name) is None

    def test_add_book_in_favorites_can_add_book(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites.count(name)

    def test_get_list_of_favorites_added_books_in_favorites_in_list(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        name2 = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(name)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name2)
        assert name, name2 in collector.get_list_of_favorites_books

    def test_delete_book_from_favorites_check_than_list_have_not_deleted_book(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites.count(name) == 0

    def test_set_book_rating_added_book_changed_rating(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_rating(name, 4)
        assert collector.get_book_rating(name) == 4

    def test_get_books_with_specific_rating_list_with_rating_six(self):
        collector = BooksCollector()
        name = 'Азбука'
        collector.add_new_book(name)
        collector.set_book_rating(name, 4)
        name2 = 'Вторая'
        collector.add_new_book(name2)
        collector.set_book_rating(name, 6)
        name3 = 'Синяя'
        collector.add_new_book(name3)
        collector.set_book_rating(name, 6)
        assert name2, name3 in collector.get_books_with_specific_rating(6)


    def test_add_new_book_cant_add_same_book_two_time(self):
        collector = BooksCollector()
        name = 'Азбука'
        collector.add_new_book(name)
        collector.set_book_rating(name, 4)
        collector.add_new_book(name)
        assert collector.get_book_rating(name) == 4