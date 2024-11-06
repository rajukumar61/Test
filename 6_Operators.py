# ---------- Arithmatic Operator ------------
'''
+ - * /
// -> integer division, rounded down towards minus infinity
% -> modulo, the remainder after integer division
'''

a = 12
b = 5
print(f"Addition: {a+b}")
print(f"Substraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Integer Division: {a//b}")
print(f"Modulo (Remainder): {a%b}")

# ------------Operator Precedence------------------------
# (), / * // %, + -
# left to right precedence order

# BEDMAS - Brackets, Exponets, Division/Multiplication, Addition/Substraction

print(a + b / 3 - 4 * 12)

result = 10 + 5 * (2 % 3) - 4 // 2
print(result)

result = 10 + 5 * 2 % 3 - 4 // 2
print(result)