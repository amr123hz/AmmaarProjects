from random import randint

end = False

choice = input("do you want to role the dice y/n") 
if choice  == "n":
    print("Thanks for playing!  ") 
    end = True 
elif choice == "y":
    num1 = randint(1,5) +1
    num2 = randint(1,5) + 1
    print("("+str(num1) + "," +str(num2),")")
else :
    print("please enter a valid choice  ") 

while end == False :
    
    choice = input("do you want to role the dice y/n  ") 
    if choice  == "n":
        print("Thanks for playing!  ") 
        end = True 
    elif choice == "y":
        num1 = randint(1,5) +1
        num2 = randint(1,5) + 1
        print("("+str(num1) + "," +str(num2),")")
    else :
        print("please enter a valid number ") 
 