import random 
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"enter no from 1 to {x} : "))
        if guess < random_number:
            print("sorry ,try again . Too low")
        elif guess > random_number:
            print("sorry try again . Too high")
    print("yay congrats! you guess the no correct")
    
g = guess(10)    