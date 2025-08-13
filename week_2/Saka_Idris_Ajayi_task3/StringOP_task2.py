# String Operations Practice Questions
# Task2


# 6. Check if a given string contains the substring "python" (case-insensitive).
strtxt = "python"
print("python" in strtxt.lower())

text = "I love Python programming"
print("python" in text.lower())


# if "python" == strtxt.lower:{
#     print("The string contains 'python'.")
# }
# else:{
#     print("The string does not contain 'python'.")

# }
# #===============OR
# if "python" in text.lower():
#     print("The string contains 'python'.")
# else:
#     print("The string does not contain 'python'.")


# 7. Write a program to reverse a string without using Indexing ([::-1]).

print(''.join(reversed("Python")))

# ================== OR ============
word = "Python"
txtIndexing_1 = (word[-1]) # n for Python
txtIndexing_2 = (word[-2]) # o for Python
txtIndexing_3 = (word[-3]) # h for Python
txtIndexing_4 = (word[-4]) # t for Python
txtIndexing_5 = (word[-5]) # y for Python
txtIndexing_6 = (word[-6]) # p for Python
print(txtIndexing_1 + txtIndexing_2 + txtIndexing_3 + txtIndexing_4 + txtIndexing_5 + txtIndexing_6)





# 8. Given a string with extra spaces, remove the leading and trailing spaces.

text = "  LOVE  "
print(text.strip())



# 9. Ask the user to enter a sentence and print the number of vowels in it.

# Ask the user to enter a sentence

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(map(sentence.count, vowels))
print("Number of vowels:", count)

# ===============OR =================
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in sentence if char in vowels)

print("Number of vowels:", count)



# txtName = input("Enter your fistname: ")
# # txtFirstName = input("Enter your fistname: ")
# print(len(txtName))





# 10. Convert a string "1234" to an integer and multiply it by 2.
valStr = "1234"
result = int(valStr) * 2
print(result)  
# ===============OR =================
val1 = 1
val2 = 2
val3 = 3
val4 = 4
mulva1 = val1 * 2 # Output: 2
mulva2 = val2 * 2 # Output: 4
mulva3 = val3 * 2 # Output: 6
mulva4 = val4 * 2 # Output: 8

print(val1, "* 2 = ", mulva1)
print(val2, "* 2 = ", mulva2)
print(val3, "* 2 = ", mulva3)
print(val4, "* 2 = ", mulva4)
