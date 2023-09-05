num = int(input("Enter a number: "))

num_str = str(num)
is_palindrome = num_str == num_str[::-1]
if is_palindrome:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

digit_occurrences = {}
for digit in num_str:
    digit_occurrences[digit] = digit_occurrences.get(digit, 0) + 1

print("Digit occurrences:")
for digit, count in digit_occurrences.items():
    print(f"Digit {digit}: {count}")
