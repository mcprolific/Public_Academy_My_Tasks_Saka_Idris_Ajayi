print("Task 6: Word Analyzer \n")

print("A. Ask the user to input a word. \n")
txtWord = input("Enter any word word: ")

print("B. Print the length of the word. \n")
print(f"Length of the word: {len(txtWord)} words.")


print("c. Check if it is all uppercase, all lowercase, or title case. \n")
if txtWord.isupper():
    print("The word is in uppercase.")
elif txtWord.islower():
    print("The word is in lowercase.")
elif txtWord.istitle():
    print("The word is in title case.")
else:
    print("The word has a mixed case.")

print("D. Reverse the word using slicing. \n")

reversed_word = txtWord[::-1]
print(f"Reversed word: {reversed_word}")

