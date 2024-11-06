# -------Escape Character--------
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

print("Number 1 \tThe Larch\nNumber 2 \tThe Horse Chestnut")

''' 
    '\' is being used to escape the charactrs but what if we want to include this backslash in our string
    - we use 'r' i.e rule before double qutoation like (r"your strings here") for the same 
'''

# print("c:\user\timbuchalka\notes.text")
print("c:\\user\\timbuchalka\\notes.text")
print(r"c:\user\timbuchalka\notes.text")

