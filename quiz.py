# Quiz Game
# Author:
# Date: Dec. 4 /2020

quiz_score = 0

# Question 1

q1 = int(input("1 - 1"))
if q1 == 0:
    print("You are correct.")
    quiz_score += 1

elif q1 != 0:
    print("You are incorrect the answer is 0.")
    quiz_score = 0

# Question 2

q2 = int(input("2 - 1"))
if q2 == 1:
    print("You are correct.")
    quiz_score += 1

elif q2 != 1:
    print("You are incorrect the answer is 1.")
    quiz_score = 0

# Question 3

q3 = int(input("3 - 1"))
if q3 == 2:
    print("You are correct.")
    quiz_score += 1

elif q3 != 2:
    print("You are incorrect the answer is 2.")
    quiz_score = 0

# Question 4

q4 = int(input("4 - 1"))
if q4 == 3:
    print("You are correct.")
    quiz_score += 1

elif q4 != 3:
    print("You are incorrect the answer is 3.")
    quiz_score = 0

# Question 5

q5 = int(input("5 - 1"))
if q5 == 4:
    print("You are correct.")
    quiz_score += 1

elif q5 != 4:
    print("You are incorrect the answer is 4.")
    quiz_score = 0

# print out the score
print(f"you got {quiz_score} out of 5.")

