print("Task6 \n")

print("The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement.  \n")

print("For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME.  \n")

# Breakdown of the Admission Process:
# Step 1: Age check
age = int(input("Enter your age to check if you are eligible : "))
if age < 16:
    print("Not eligible: Minimum admission age is 16 years.")
    exit()
elif age > 16:
    print("You are welcome to continue your processing")

# 1. UTME:
# Candidates must score 200 or above in the UTME and choose UNILAG as their first choice.
utme_score = int(input("Enter your UTME score: "))
if utme_score < 200:
    print("Not eligible: Minimum UTME score required is 200.")
    exit()
elif utme_score > 199:
    print("You enable to continue your processing.")


# 2. O'Level Requirements:
# Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
olevel_pass = input("Do you have at least 5 credit passes in one sitting (including English and Maths)? (yes/no): ").lower()
if olevel_pass != "yes":
    print("Not eligible: You must have at least 5 O'Level credits including English and Maths in one sitting.")
    exit()
elif olevel_pass == "yes":
    print("You have 5 O'Level credits including English and Maths in one sitting")


# 3. Post-UTME:
# Eligible candidates participate in the university's online Post-UTME screening. 
post_utme = int(input("Enter your Post-UTME score: "))

# 4. Departmental Cut-off Marks:
# After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
# (This can range from 200 to 320). 
dept_cutoff = int(input("Enter the departmental cut-off mark (between 200 and 320): "))


# 5. Final Admission:
# Candidates who meet the departmental cut-off marks are offered admission. 
final_score = (utme_score + post_utme) / 2  # Average of UTME and Post-UTME
print(f"\nYour Final Admission Score: {final_score}")

if final_score >= dept_cutoff:
    print("Congratulations! You are eligible for admission into UNILAG.")
else:
    print("Sorry, you did not meet the departmental cut-off mark.")


# - Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.