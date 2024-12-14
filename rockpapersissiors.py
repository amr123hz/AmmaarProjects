from random import randint
number = randint(0,2)
choice = ["r","p","s"]
# r > s 
# r< p
# p< s 
continue1   = True
incorrectcont = True  
while incorrectcont == True :
    iscontinue = input("do you want to continue y/n")
    if iscontinue == "y"  or iscontinue =="n":
        incorrectcont = False
        if iscontinue == "n" :
            continue1 = False 
while continue1 == True :
    choiceh = input("please enter your choice")
    choicec =    choice[randint(0,2)]
    if choiceh == "r" and choicec =="r":
        print("draw " ) 
    elif choiceh == "r" and choicec =="s":
        print("you won")
    elif choiceh == "r" and choicec =="p":
        print("you lost ")
    elif choiceh == "p" and choicec =="r":
        print("you won")
    elif choiceh == "p" and choicec =="p":
        print("draw")
    elif choiceh == "p" and choicec =="s":
        print("you lost ")
    elif choiceh == "s" and choicec =="r":
        print("you lost")
    elif choiceh == "s" and choicec =="s":
        print("draw ")
    elif choiceh == "s" and choicec =="p":
        print("you won")
    continue1   = True
    incorrectcont = True  
    while incorrectcont == True :
        iscontinue = input("do you want to continue y/n")
        if iscontinue == "y"  or iscontinue =="n":
            incorrectcont = False
            if iscontinue == "n" :
                continue1 = False 

