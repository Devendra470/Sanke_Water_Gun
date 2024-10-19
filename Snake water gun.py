import random 
def gamewin(player,comp):
    if player=="s":
        if comp=="w":
            return True
        elif comp=="g":
            return False
    if player=="w":
        if comp=="s":
            return False
        elif comp=="g":
            return True
    if player=="g":
        if comp=="s":
            return True
        elif comp=="w":
            return False
    if player==comp:
        return None
randno=random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"
player=input("Your Move: snake(s),water(w) or gun(g): ")
a=gamewin(player,comp)
if a==None:
    print("It's a tie!")
elif a:
    print("You Won!")
elif a==False:
    print("You loose!")
print(f"You choose: {player}")
print(f"Computer choose: {comp}")
