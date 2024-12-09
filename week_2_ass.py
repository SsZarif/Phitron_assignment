# answer 1:
class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_all_books(cls):
        for book in cls.book_list:
            book.view_book_info()
            print("------------------------")

    @classmethod
    def borrow_book(cls):
        try:
            book_id = int(input("Enter the book ID to borrow: "))
            for book in cls.book_list:
                if book.get_book_id() == book_id:
                    book.borrow_book()
                    return
            raise ValueError("Book not found in the library.") # Answer 8
        except ValueError as e:
            print(e)

    @classmethod
    def return_book(cls):
        try:
            book_id = int(input("Enter the book ID to return: "))
            for book in cls.book_list:
                if book.get_book_id() == book_id:
                    book.return_book()
                    return
            raise ValueError("Book not found in the library.") # Answer 8
        except ValueError as e:
            print(e)

    # Answer 8:
    @classmethod
    def start_menu(cls):
        while True:
            try:
                print("Library Menu:")
                print("1. View All Books")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    cls.view_all_books()
                elif choice == "2":
                    cls.borrow_book()
                elif choice == "3":
                    cls.return_book()
                elif choice == "4":
                    print("Exiting the library. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print("An error occurred:", str(e))

# Answer 2:
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id 
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def get_book_id(self):
        return self.__book_id

    # Answer 4:    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You have borrowed '{self.__title}' by {self.__author}.")
        else:
            print(f"Sorry, '{self.__title}' by {self.__author} is not available for borrowing.") # Answer 8

    # Answer 5:
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have returned '{self.__title}' by {self.__author}.")
        else:
            print(f"'{self.__title}' by {self.__author} is already available.")

    # Answer 6:
    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {availability_status}")


book1 = Book(1, "Data Structure", "Kodom ali")
book2 = Book(2, "Algorithm", "osama bin lagging")
book3 = Book(3, "English grammer", "donald trump")
book4 = Book(4, "Bangla grammar", "sakib al hasan")
book5 = Book(5, "linear algebra", "elon task")
book6 = Book(6, "Operating System", "sir alex ferguson")
book7 = Book(7, "Computer Network", "cristiano ronaldo")
book8 = Book(8, "Database harasement", "lionel messi")
book9 = Book(9, "Computer Organization", "lebron james")
book10 = Book(10, "Statistics", "tiger woods")

Library.start_menu()

