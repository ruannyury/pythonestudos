# Bitwise Operators
bin_num = bin(int(input('Input a number: ')))
print(f'Binary output (of the number inputed) = {bin_num}')
# In the output, the first two characters ‘0b’ are there to represent the
# binary data in the string. Remaining character string ‘10101’ is the
# actual value when you convert an integer value to binary.

# Bitwise AND in python:
a = 213  # 11010101
b = 15  # 00001111
print('a = ', a)
print('b = ', b)
print('a & b = ', a & b)  # Só teremos 1 quando ambos forem 1.

# Bitwise OR in python:
a = 4
b = 5
print("a = ", a)
print("b = ", b)
print("a | b = ", a | b)  # Basta um deles ser 1 que o "resultado" será 1.

# Bitwise NOT in python:
a = 4
print("a = ", a)
print("~a = ", ~a)  # Inverte os bits. 0 ira 1 e vice versa

# Bitwise XOR in Python:
a = 4
b = 5
print("a = ", a)
print("b = ", b)
print("a ^ b = ", a ^ b)  # Se os bits forem iguais, zero, se diferentes, um

# Bitwise Right Shift in Python:
a = 4
print("a = ", a)
print("a >> 1 = ", a >> 1)  # Move os bits 1 para a direita 'n' casas

# Bitwise Left Shift in Python:
a = 4
print("a = ", a)
print("a << 1 = ", a << 1)  # Move os bits 1 para a esquerda 'n' casas
