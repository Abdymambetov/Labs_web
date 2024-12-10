
class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.is_issued = False

    def __str__(self):
        status = "Выдана" if self.is_issued else "Доступна"
        return f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}, ID: {self.book_id}, Статус: {status}"

    def change_status(self):
        self.is_issued = not self.is_issued


class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.issued_books = []

    def add_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        self.issued_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def issue_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not user:
            print("Пользователь не найден.")
            return
        if not book:
            print("Книга не найдена.")
            return
        if book.is_issued:
            print("Книга уже выдана.")
            return

        book.change_status()
        user.add_book(book)
        print(f"Книга '{book.title}' выдана пользователю '{user.username}'.")

    def return_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not user:
            print("Пользователь не найден.")
            return
        if not book:
            print("Книга не найдена.")
            return
        if book not in user.issued_books:
            print("Эта книга не была выдана этому пользователю.")
            return

        book.change_status()
        user.return_book(book)
        print(f"Книга '{book.title}' возвращена пользователем '{user.username}'.")


def main_menu():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Зарегистрировать пользователя")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Посмотреть все книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            book_id = len(library.books) + 1  # Присвоение уникального ID
            book = Book(title, author, year, book_id)
            library.add_book(book)
            print(f"Книга '{title}' добавлена в библиотеку.")

        elif choice == '2':
            username = input("Введите имя пользователя: ")
            user_id = len(library.users) + 1  # Присвоение уникального ID
            user = User(username, user_id)
            library.register_user(user)
            print(f"Пользователь '{username}' зарегистрирован.")

        elif choice == '3':
            user_id = int(input("Введите ID пользователя: "))
            book_id = int(input("Введите ID книги: "))
            library.issue_book(user_id, book_id)

        elif choice == '4':
            user_id = int(input("Введите ID пользователя: "))
            book_id = int(input("Введите ID книги: "))
            library.return_book(user_id, book_id)

        elif choice == '5':
            print("\nСписок книг в библиотеке:")
            for book in library.books:
                print(book)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
