from abc import ABC, abstractmethod
from colorama import Fore, Style, init

init(autoreset=True)

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(Fore.GREEN + f'Book "{book.title}" added successfully!')

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(Fore.GREEN + f'Book "{title}" removed successfully!')
                return
        print(Fore.RED + f'Book "{title}" not found!')

    def show_books(self):
        if not self.books:
            print(Fore.YELLOW + "The library is empty.")
        for book in self.books:
            print(Fore.CYAN + str(book))

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input(Fore.BLUE + "Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input(Fore.BLUE + "Enter book title: ").strip()
                author = input(Fore.BLUE + "Enter book author: ").strip()
                year = input(Fore.BLUE + "Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input(Fore.BLUE + "Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print(Fore.GREEN + "Exiting the program. Goodbye!")
                break
            case _:
                print(Fore.RED + "Invalid command. Please try again.")

if __name__ == "__main__":
    main()