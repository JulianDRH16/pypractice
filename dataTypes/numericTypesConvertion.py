number_input = int(input("Write a integer number in base 10: "))

binary_number = format(number_input, 'b')
binary_number2 = bin(number_input)

octal_number = format(number_input, 'o')
octal_number2 = oct(number_input)

hexa_number = format(number_input, 'x')
hexa_number2 = hex(number_input)

print("binary_number_format--->", binary_number)
print("binary_number2--->", binary_number2)
print("octal_number_format ---->", octal_number)
print("octal_number2 ---->", octal_number2)
print("hexa_number_format ----->", hexa_number)
print("hexa_number2 ----->", hexa_number2)