def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print("Decimal equivalent:", decimal_output)

octal_input = input("Enter an octal number: ")
hexadecimal_output = octal_to_hexadecimal(octal_input)
print("Hexadecimal equivalent:", hexadecimal_output)