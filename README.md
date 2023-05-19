# qa_python

## 1. test_add_new_book_add_two_books
Тест проверяет метод _add_new_book_. Добавлят две книги и проверяет, что добавилось именно две книги.

## 2. test_get_book_rating_add_new_book_twice
Тест проверяет метод _get_book_rating_. Добавляет две книги с одинаковым названием и проверяет, что в словарь добавилась только одна книга.

## 3. test_get_book_rating_add_new_book_rating_one
Тест проверяет метод _get_book_rating_. Добавляет новую книгу и проверяет, что у новой книги рейтинг 1.

## 4. test_add_new_book_rating_not_exist
Тест проверяет метод _add_new_book_. Добавляет новую книгу и проверяет, что у новой книги рейтинг не пустое значение.

## 5. test_set_book_rating_change_rating_seven
Тест проверяет метод _set_book_rating_. Добавляет новую книгу и присваивает ей новый рейтинг 7, проверяет, что рейтинг книги равен 7.

## 6. test_get_books_with_specific_rating_rating_seven_two_books
Тест проверяет метод get_books_with_specific_rating. Добавляет две книги с одинаковым рейтингом и третью с другим рейтингом, проверяет, что количество книг с одинаковым рейтингом две.

## 7. test_add_book_in_favorites_add_one_book_in_favorites_one_book
Тест проверяет метод _add_book_in_favorites_. Добавляет книгу в словарь и из словаря в избранное и проверяет, что количество книг в избранном один.

## 8. test_add_book_in_favorites_add_book_book_in_favorites
Тест проверяет метод _add_book_in_favorites_. Добавляет книгу в словарь и из словаря в избранное и проверяет, что книга с определенным названием существует в списке избранное.

## 9. test_delete_book_from_favorites_delete_book_book_not_in_favorites
Тест проверяет метод _delete_book_from_favorites_. Добавляет книгу в словарь и из словаря в избранное, затем удаляет книгу из избранного. Проверяет, что книга с определенным названием отсутствует в избранном.

## 10. test_get_list_of_favorites_books_add_all_books_in_favorites_in_favorites_and_in_rating_same_books
Тест проверяет метод _get_list_of_favorites_books_. Добавляет две книги в словарь и их же в избранное, проверяет, что в словаре и в избранном содержатся одни и те же книги.
