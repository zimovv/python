from random import randint

print("Guess what number I am thinking (0~100)")
num = randint(0,100)

result = False
while result==False:
    inNum = eval(input())
    
    if inNum > num:
        print("too big")
    elif inNum < num:
        print("too small")
    else:
        print("Yes!")
        result = True
