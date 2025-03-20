"""In class tasks
TASK 1: Create a rectangle class. Here are the requirements:

- Define a class named Rectangle.
- The class should have two instance attributes: width and height.
- Add a method named area that returns the area of the rectangle.
- Add a method named perimeter that returns the perimeter of the rectangle.

"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        print("Width and height are set.")

    def area(self) -> int:
        return self.width * self.height
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)
    
my_rectangle = Rectangle(4, 2)
print(my_rectangle.width)
print(my_rectangle.height)
print(my_rectangle.area())
print(my_rectangle.perimeter())

"""
TASK 2: Create a Book Class

- Define a class named Book
- The class should have three instance attributes: title, author, and pages
- Add a method named description that returns a string with the book's title, author, and number of pages.

"""
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"{self.title} by {self.author} has {self.pages} pages")

my_book = Book("1984", "George Orwell", "300")
my_book.description()

"""
WEEK 9 POST CLASS TASK: BankAccount Class

Define a class named BankAccount. Here are the requirements:

- The class should have an instance attribute balance initialized to 0.
- Add a method named deposit that takes an amount and adds it to the balance.
- Add a method named withdraw that takes an amount and subtracts it from the balance if there are sufficient funds.
- Add a method named get_balance that returns the current balance.

"""

class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance
        print(f"Your account has been created and has ${self.balance}.")
    
    def deposit(self, amount: int):
        self.balance += amount
        print(f"${amount} has been added to your account. The new balance is ${self.balance}.")
    
    def withdraw(self, amount: int):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account. The new balance is ${self.balance}.")
    
    def get_balance(self) -> int:
        print(f"Your bank account currently has ${self.balance}")
        return self.balance
    
my_bank_account = BankAccount(100)
my_bank_account.deposit(100)
my_bank_account.withdraw(250)
my_bank_account.withdraw(50)
my_bank_account.get_balance()