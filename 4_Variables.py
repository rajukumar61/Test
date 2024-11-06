#-------------- Variables---------------
'''
python variables used to allocate memory for us and store the value


rules for variable naming -
    - must start with a letter or an underscore _ character
    - it can contain letters, numbers or underscore characters but not in the begining
    - variable names are case sensitive, Greetings & greetings are different
'''

greeting = "Hello"
name = input("Please enter your name: ")

print(greeting + ' ' + name)

num1 = 20
num2 = 2342.342

sum = num1 + num2
print(f"Sum of {num1} and {num2} is : {sum}")

# data types - use type() function to get the data type of a variable
print(type(greeting))
print(type(num2))
print(type(num1))
print(type(sum))

# in python, we can reassign the value, it will not show errors like the variable is already created
age = 293
print(age)
print(type(age))

age = "293 years"
print(age)
print(type(age))


# python is a strongly typed programming language
'''
Here’s what makes Python strongly typed:
1. No Implicit Type Conversion:
    - Python doesn't automatically convert types in a way that could lead to data loss or unexpected behavior. 
    - For example, you can't just add an integer to a string in Python. You need to explicitly convert types if you want to perform certain operations:

2. Explicit Casting Required:
    - Python requires explicit type conversions when interacting with different data types. 
    
3. Dynamic Typing vs. Strong Typing:
    - Although Python is dynamically typed (meaning you don't need to declare a variable's type explicitly), 
    - it remains strongly typed. The dynamic aspect allows flexibility with types, 
    - but the strong typing ensures that Python won’t mix types without explicit instruction.
'''

# This will raise a TypeError in Python:
# result = "Number: " + 5
# To make it work, you must do an explicit conversion:
result = "Number: " + str(5)
print(result)
