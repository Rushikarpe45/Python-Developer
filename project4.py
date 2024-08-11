#Create a program capable of displaying question to the user like KBC>
#use List data type to store the question and their correct answers.
#Display the final amount the person is taking home after playing the game


questions = [
    
["which language was used to create fb?","Python","French","javascript","php","None",4]

]

levels =[1000,2000,3000,5000,10000,20000,40000,
80000,160000,320000 ]


for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for  Rs. {levels[i]}" )
    print(f"a.{question[1]}       b.{question[2]} " )
    print(f"c.{question[3]}       d.{question[4]} " )
    reply = int(input(" Enter your answer(1-4)  or 0 to quit " ))
    if(reply == question4[-1]):
        print(f" Correct answer, you have won RS. {levels[i]} ")
        if(i == 4):
            money = 1000
        elif(i==9):
            money=320000
        elif(i== 9):
            money = 1000000

    else:
        print("wrong answer!")
        break

print("your take home money is {money}")
