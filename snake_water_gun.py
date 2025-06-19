import random

def compinp():

    game=random.choice(["snake", "gun", "water"])
    return game
    
def userinp():
    user=input("enter user input (snake,water,gun)").lower()
    while user not in ["snake", "gun", "water"]:
        print("invalid")
        user=input("enter user input (snake,water,gun)").lower()
    return user

def match(compchoice,userchoice):
    if(compchoice==userchoice):
        print("Draw")
        
    elif(compchoice=="snake" and userchoice=="water")or(compchoice=="gun" and userchoice=="snake")or(compchoice=="water" and userchoice=="gun"):
        print("Computer Wins")

    else:
        print("User Wins")


n=int(input("no. of matches"))

for i in range(1,n+1):
    print(f"Match-{i} \n")
    compchoice=compinp()
    userchoice=userinp()
    print(f"Computer chose= {compchoice}")
    print(f"User chose= {userchoice}")
    match(compchoice,userchoice)


