class PalindromeChecker:
    def __init__(self):
        self.isPalindrome = False

    def check(self, input):
        self.isPalindrome = str(input) == str(input)[::-1]
        return self.isPalindrome

st = input("Enter a string: ")
stObj = PalindromeChecker()
if stObj.check(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

val = input("Enter an integer: ")
intObj = PalindromeChecker()
if val.isdigit() and intObj.check(int(val)):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")
