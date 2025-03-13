# Classes + Objects in Python

"""
CLASSES + OBJECTS DEFINITIONS

Classes are blueprints for creating objects.
A class defines a set of attributes and methods that the created objects (instances) will have. 
You can think of a class as a "definion" for objects.

Objects are instances of classes. When you create an object, you are instantiating a class. 
Each object can have its own unique values for the attributes defined in the class.

For example, let's say we have a class Car that defines the attributes and methods for a car.

"""

class Car:
    def __init__(self, make):
        self.make = make

    def display_info(self):
        print(f"{self.make}") 
        # In order to use the make attribute in the function, I need to have "self" as a parameter here

"""
In this example:

- The function "__init__" is a special method called a constructor. It initializes the object's attributes.
    - For classes that need to be initialized with initial values, you'll need a constructor.
- "self" is a reference to the current instance of the class. It is used to access variables that belong to the class.
    - If you're confused about self, watch this: https://www.youtube.com/watch?v=oaiQ5hYKHTE 
- "make" is an attribute of the class in this example
- The function "display_info" is a method that prints out the car's information in this example
    - You'll (usually) need to put in self as the first parameter in a method defined within a class
"""

"""
Creating Objects
Now, let's create some objects (instances) of the Car class.
"""

# Creating instances of the Car class
car1 = Car("Toyota") # The string "Toyota" represents the argument "make" in the __init__ function
car2 = Car("Honda")

# Accessing attributes and methods
car1.display_info()  # Output: Toyota
car2.display_info()  # Output: Honda


"""
In this example:

car1 and car2 are objects of the Car class.
We call the display_info method on each object to print their information.
"""

"""
Summary
- Class: A blueprint for creating objects.
- Object: An instance of a class.
- Attributes: Variables that belong to a class.
- Methods: Functions that belong to a class.
"""