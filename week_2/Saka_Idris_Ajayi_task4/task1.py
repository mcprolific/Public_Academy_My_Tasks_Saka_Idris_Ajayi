print("TASK 1. Your Favorite Life Quote \n")

print("A. Ask the user to input their favorite quote.\n")
print("Good morning guys!")
strSentence = str(input("please, enter your favorite quote here: "))
print(strSentence)



print("B. Convert it to title case. \n")
print(strSentence.title())



print("C. Print it with quotation marks using escape sequences. \n")

strSentence2 = str(input("Enter another favorite quote here: "))

print("For examples of escape sequences in print - \"\\n\", \"\\t\", \"\\n\"")

print("quotation 1: " + strSentence + "\n" + "quotation 2: " + strSentence2)              # New line

print(strSentence + "\t, " + strSentence2)              # Tab space

print("He said, \"" + strSentence +"\"")        # Quoted string


