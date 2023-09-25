"""this is a timed math challenge programme
the user will have to answer a couple of random expressions 
with a timer who """


import random
import time

operations=["+","-","*"]
min_number = 3
max_number = 12
total_problem = 10

def generate_problem():
    left = random.randint(min_number,max_number)
    right = random.randint(min_number,max_number)
    operation = random.choice(operations)
    
    expr = str(left) +" "+ operation +" "+ str(right)
    answer= eval(expr)
    return expr,answer

wrong = 0
input("press enter to start: ")
print("-----------------------")

start_time = time.time()

for i in range(1,total_problem+1):
    expr, answer = generate_problem()
    while True :
        guess = input(f"problem #{str(i)} : {expr} =")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()

total_time = round(end_time - start_time,3)

print("-----------------------")
print(f"nice work! you finished in {total_time} secondes")
if(wrong==0):
    print("congratulations ! you completed the challenge without any mistake")
else:
    print(f"not bad ! you completed the challenge with {total_problem - wrong} correct answers")