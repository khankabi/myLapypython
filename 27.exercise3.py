#write a program of capable of displaying question to the user like KBC.
questions=["question 1",
           "question 2",
           "question 3"]
solutions=["sol1",
           "sol2",
           "sol3"]
prize=[1000,5000,10000]
count=0
i=0
while(True):
    print(questions[i])
    ans=input("enter your answer:")
    if(ans==solutions[i]):
        print("congratulations !!!")
        count=count+prize[i]
        i=i+1
    else:
        print("wrong answer !!!")
        break
print("thank you")