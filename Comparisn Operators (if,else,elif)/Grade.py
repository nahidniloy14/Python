"""
✅ Requirements:
Input: An integer score between 0 and 100.

Output:

A letter grade (A, B, C, D, F).

If the grade is A, and the score is 95 or above, also print: "Excellent performance!"

If the grade is F, and the score is below 40, print: "Needs serious improvement."

Use nested if conditions to implement the extra feedback.

"""
score=int(input("Enter score: "))
if 0<=score<=100:
    if score >= 90:
        print("Grade: A")
        if score >=95:
            print("Excellent performance!")
    elif score >40 and score <90:
        print("Try Hard!!")
    elif score <= 40:
        print("Needs serious improvement")
else:
    print("Invalid")