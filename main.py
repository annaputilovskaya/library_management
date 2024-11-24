from src.library import Library


def user_interaction():
    """
    Функция взаимодействия с пользователем.
    """
    library = Library()

    while True:
        print(
            "\n1. Добавить книгу"
            "\n2. Удалить книгу"
            "\n3. Найти книгу"
            "\n4. Показать все книги"
            "\n5. Изменить статус книги"
            "\n0. Выход"
        )
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Название книги: ")
            author = input("Автор книги: ")
            year = input("Год издания: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = input("Введите id книги для удаления: ")
            library.delete_book(book_id)

        elif choice == "3":
            query = input("Введите запрос для поиска: ")
            filter_by = input(
                "Поиск по:"
                "\nназванию книги - введите 1"
                "\nавтору - введите 2"
                "\nгоду издания - введите 3"
                "\nили нажмите любую другую клавишу: "
            )
            results = library.get_books_by_query(query, filter_by)
            if results:
                [print(book) for book in results]
            else:
                print("Книг по указанному запросу не найдено.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = input("Введите id книги для изменения статуса: ")
            status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, status)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    user_interaction()
