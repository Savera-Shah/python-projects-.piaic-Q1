import random 

def comp_guess(x):
    low = 1
    high = x
    feedbac=''
    while feedbac != 'c':
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        feedbac =input(f"the  {guess } is low(l), is high(h) and is correct(c)" ).lower()
        if feedbac == 'h':
            guess= high - 1
        elif feedbac == 'l':
            guess = low + 1
    print("yay congrats! you guess the no correct")
s=comp_guess(10)        
       