# String Operations Practice Questions

# Task3: Pattern Matching & Splitting
# 11. Given "apple,banana,orange", split the string into a list of fruits.

fruits = "apple,banana,orange"
print(fruits.split(","))


# 12. Ask the user for a sentence and print each word on a new line.

sentence = input("Enter a sentence: ")
print(*sentence.split(), sep="\n")

# ===============OR =================

sentence = input("Enter a sentence: ")
list(map(print, sentence.split()))

# 13. Replace all spaces in a string with underscores (_).

txtStr = "Replace all spaces in a string with underscores"
result = txtStr.replace(" ", "_")
print(result)

# ===============OR =================

text = "Splits a string into a list using a separator (default is space)"
result = "_".join(text.split(" "))
print(result)

# 14. Count how many times the letter "a" appears in "Banana".
word = "Banana"
count = word.lower().count('a')
print(count)

# 15. Check if a given string starts with "https://".

url = "https://publica.academy/courses"
print(url[:8] == "https://")

# ===============OR =================

url = "https://publica.academy/courses"
print(url.startswith("https://"))

# ===============OR =================

url = "https://publica.academy/courses"
print(url.find("https://") == 0)