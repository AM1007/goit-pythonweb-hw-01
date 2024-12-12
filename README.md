# SOLID Principles

## Homework consists of two tasks.

Both tasks require the use of type annotations. Instead of the `print` operator, use logging at the `INFO` level. Use `black` for code formatting.

---

## Technical Description of Tasks

---

### Task 1. Factory Pattern

The following code represents a simple system for creating vehicles. We have two classes: `Car` and `Motorcycle`. Each class has a `start_engine()` method that simulates starting the engine of the respective vehicle. Currently, to create a new vehicle, we simply instantiate the respective class with the given `make` and `model`.

```python
    class Car:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def start_engine(self):
            print(f"{self.make} {self.model}: Двигун запущено")

    class Motorcycle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def start_engine(self):
            print(f"{self.make} {self.model}: Мотор заведено")

    # Usage
    vehicle1 = Car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()
```

The next step is to create vehicles considering the specifications of different regions, such as `US Specs` for the USA and `EU Specs` for Europe.

**Your task** is to implement the factory pattern to create vehicles with different regional specifications without modifying the core vehicle classes.

#### Steps to complete Task 1:

1.  Create an abstract base class `Vehicle` with a method `start_engine()`.
2.  Modify the `Car` and `Motorcycle` classes so they inherit from `Vehicle`.
3.  Create an abstract class `VehicleFactory` with methods `create_car()` and `create_motorcycle()`.
4.  Implement two factory classes: `USVehicleFactory` and `EUVehicleFactory`. These factories should create cars and motorcycles marked with the region specification, e.g., `Ford Mustang (US Spec)` for the USA.
5.  Refactor the initial code to use factories for creating vehicles.

**Expected Result:**

Code that enables creating vehicles for different regions easily using the respective factories.

---

### Task 2. SOLID Principles

Below is a simplified program for managing a library of books. The program allows adding new books, removing books, and displaying all books in the library. Users can interact with the program through the command line using the commands `add`, `remove`, `show`, and `exit`.

```python
    class Library:
        def __init__(self):
            self.books = []

        def add_book(self, title, author, year):
            book = {
                "title": title,
                "author": author,
                "year": year
            }
            self.books.append(book)

        def remove_book(self, title):
            for book in self.books:
                if book["title"] == title:
                    self.books.remove(book)
                    break

        def show_books(self):
            for book in self.books:
                print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

    def main():
        library = Library()

        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                library.add_book(title, author, year)
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                library.remove_book(title)
            elif command == "show":
                library.show_books()
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")

    if __name__ == "__main__":
        main()
```

Your task is to refactor the code to comply with the SOLID principles.

### Steps to complete Task 2:

1.  To follow the Single Responsibility Principle (SRP), create a `Book` class responsible for storing book information.
2.  To ensure the Open/Closed Principle (OCP), make the `Library` class extensible for new functionality without modifying its code.
3.  To adhere to the Liskov Substitution Principle (LSP), ensure that any class inheriting from the `LibraryInterface` can replace the `Library` class without breaking the program.
4.  To comply with the Interface Segregation Principle (ISP), use a `LibraryInterface` to define clear methods necessary for working with the `library`.
5.  To follow the Dependency Inversion Principle (DIP), ensure that high-level classes, such as `LibraryManager`, depend on abstractions (interfaces) rather than specific implementations of classes.

```python
    from abc import ABC, abstractmethod

    class Book:
        pass

    class LibraryInterface(ABC):
        pass

    class Library(LibraryInterface):
        pass

    class LibraryManager:
        pass

    def main():
        library = Library()
        manager = LibraryManager(library)

        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            match command:
                case "add":
                    title = input("Enter book title: ").strip()
                    author = input("Enter book author: ").strip()
                    year = input("Enter book year: ").strip()
                    manager.add_book(title, author, year)
                case "remove":
                    title = input("Enter book title to remove: ").strip()
                    manager.remove_book(title)
                case "show":
                    manager.show_books()
                case "exit":
                    break
                case _:
                    print("Invalid command. Please try again.")

    if __name__ == "__main__":
        main()
```
