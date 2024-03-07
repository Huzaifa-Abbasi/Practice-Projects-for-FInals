'''Simple Quiz:
1.Create a program that asks the user 5 multiple-choice questions with three answer options each.
2.Store the correct answers in a separate list.
3.After the user answers all questions, calculate the user's score and display a message indicating their performance.'''

score = 0
list = ["python","artificial intelligence","html","bill gates","mark"]

print("Which language are you learning now:")
mcq1 = input("Python, html, java: ").lower()

if mcq1 in list:
    score +=1

print("A.I stands for:")
mcq2 = input("Artificial Intelligence, Air Industry, Agricultural Industry: ").lower()

if mcq2 in list:
    score +=1

print("Who is the CEO of Microsoft:")
mcq3 = input("Elon, mark, bill gates: ").lower()

if mcq3 in list:
    score +=1

print("Meta is own by:")
mcq4 = input("bill gates, mark , elon").lower()

if mcq4 in list:
    score +=1

print("Which Language is Mostly used for web development :")
mcq5 = input("Python, html, java: ").lower()

if mcq5 in list:
    score +=1
    print(f"Your Score is {score}")
else:
    print(f"Your Score is {score}")