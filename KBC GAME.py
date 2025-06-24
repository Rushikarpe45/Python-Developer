#Create a program capable of displaying question to the user like KBC>
#use List data type to store the question and their correct answers.
#Display the final amount the person is taking home after playing the game


questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", 4],
    ["What is the capital of India?", "Mumbai", "Delhi", "Pune", "Kolkata", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3]
]

levels = [1000, 2000, 3000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    if reply == 0:
        break

    if reply == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("Wrong answer!")
        break

print(f"\nYour take home money is Rs. {money}")
