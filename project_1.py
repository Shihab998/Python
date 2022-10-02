import random
def game(com,you):
    if com== you:
        return None
    elif com=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif com=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif com=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    

                            

print("Snack(s) Water(w) Gun(g)")
ranno=random.randint(1,3)
if ranno==1:
    com='s'
elif ranno==2:
    com='w'   
elif ranno==3:
    com='g'   

you=(input("Snack(s) Water(w) Gun(g) "))
a=game(com,you)
print(f'The computer choose {com} ')
print(f'The you choose {you} ')

if a== None:
    print("The game is try")
elif a:
    print("you Win")
else:
    print("You Loss")    