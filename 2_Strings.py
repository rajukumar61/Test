'''
3. Strings
    - strings can be written in single, double or triple quotes also
    - Example:
        - name = 'Raju'
        - text = "Python is fun", text2 = "Python's strings are easy"
        - sentence = """Raju said that "Python's strings are easy"."""
'''

# -----------Strings----------------

name = 'Raju'
text = "Python is fun"
text2 = "Python's strings are easy"
sentence = """Raju said that "Python's strings are easy"."""

print(name)
print(text)
print(text2)
print(sentence)

greetings = "Hello"
# name2 = input("Please enter your name: ")
# print(greetings + ' ' + name2)

# -------------------------------------------
#         01234567890123
parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[13])
# print(parrot[14])  -> out of range
print(parrot[-1]) #-> start reading from last, -1 is first index from last/reverse
print(parrot[-6]) #6th index from end/last

# NOTE:
#     - from start, first index is 0
#     - from end, first index is -1
