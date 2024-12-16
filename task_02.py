from abc import ABC, abstractmethod
from colorama import Fore, Style, init
import logging
from typing import List

init(autoreset=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"{Fore.GREEN}Book '{book.title}' added successfully!")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f"{Fore.GREEN}Book '{title}' removed successfully!")
                return
        logger.info(f"{Fore.RED}Book '{title}' not found!")

    def show_books(self) -> None:
        if not self.books:
            logger.info(f"{Fore.YELLOW}The library is empty.")
            return
        for book in self.books:
            logger.info(f"{Fore.CYAN}{str(book)}")


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input(f"{Fore.BLUE}Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input(f"{Fore.BLUE}Enter book title: ").strip()
                author = input(f"{Fore.BLUE}Enter book author: ").strip()
                year = input(f"{Fore.BLUE}Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input(f"{Fore.BLUE}Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info(f"{Fore.GREEN}Exiting the program. Goodbye!")
                break
            case _:
                logger.info(f"{Fore.RED}Invalid command. Please try again.")


if __name__ == "__main__":
    main()