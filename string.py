def count_chars(sentence):
    word_count = len(sentence.split())
    digit_count = sum(char.isdigit() for char in sentence)
    uppercase_count = sum(char.isupper() for char in sentence)
    lowercase_count = sum(char.islower() for char in sentence)
    return word_count, digit_count, uppercase_count, lowercase_count

input_sentence = input("Enter a sentence: ")
counts = count_chars(input_sentence)
print("Number of words:", counts[0])
print("Number of digits:", counts[1])
print("Number of uppercase letters:", counts[2])
print("Number of lowercase letters:", counts[3])
