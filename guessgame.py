from random import randint

number = randint(1,100)

guess = False

while guess == False:
    valid  = True 
    ans  =  int(input("please enter your guess - "))
    if (ans < 0  and  ans > 100):
        valid = False 
    while valid == False : 
        ans = int(input("please enter  a number between 1 and 100 "))
    
    if ans  == number :
        guess = True 
    elif ans > number :
        print("Too high")
    else :
        print("Too low " ) 
    
if (guess ):
    print("You guessed correct ")