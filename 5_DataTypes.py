# -----------Data Types----------

'''
String Data types:
    str

Numeric Data types:
    int
    float
    complex

Note: in python, there is no type definition before variable name, so python understand it by itself
'''

# 1. Numeric Types
'''
1. Numeric Types
    - Integer (int): Represents whole numbers (e.g., 5, -42, 2023).
    - Floating Point (float): Represents decimal numbers or numbers with fractional parts (e.g., 3.14, 0.001, -8.9).
    - Complex (complex): Represents complex numbers, with a real and an imaginary part (e.g., 3 + 5j).
'''

x = 5           # int
y = 3.14        # float
z = 2 + 3j      # complex

print(x, type(x))
print(y, type(y))
print(z, type(z))

z2 = -23 + 7j
print(f"Sum of complex numbers {z} and {z2} is : {z+z2}")
print(f"Diff of complex numbers {z} and {z2} is : {z-z2}")
print(f"Mult of complex numbers {z} and {z2} is : {z*z2}")
print(f"Div of complex numbers {z} and {z2} is : {z/z2}")


# ---------------
'''
2. Sequence Types
    - String (str): Represents text (a sequence of characters), defined within single, double, or triple quotes (e.g., "Hello", 'Python').
    - List (list): An ordered, mutable sequence of elements, which can hold elements of different types (e.g., [1, "hello", 3.5]).
    - Tuple (tuple): An ordered, immutable sequence of elements (e.g., (1, 2, "Python")).
    
    - Example:
        name = "Python"                     # str
        numbers = [1, 2, 3, 4, 5]           # list
        coordinates = (10.0, 20.0, 30.0)    # tuple
    
3. Mapping Type
    - Dictionary (dict): An unordered collection of key-value pairs, where keys are unique and can be of any immutable type (e.g., {"name": "Alice", "age": 30}).
    
    - Example:
        person = {"name": "Alice", "age": 30, "city": "New York"}
        
4. Set Types
    - Set (set): An unordered collection of unique elements, used for membership testing and removing duplicates (e.g., {1, 2, 3, 4}).
    - Frozen Set (frozenset): An immutable version of a set.
    
    - Example:
        unique_numbers = {1, 2, 3, 4, 5}       # set
        frozen_numbers = frozenset([1, 2, 3])  # frozenset
        
5. Boolean Type
    - Boolean (bool): Represents a binary value of True or False. Booleans are commonly used in conditional statements.
    
    - Example:
        is_active = True
        has_permission = False
        
7. None Type
    - None (NoneType): Represents the absence of a value, often used as a placeholder 
    - or used as default return value when a function doesn’t explicitly return anything.
    
    - Example: 
        result = None
'''