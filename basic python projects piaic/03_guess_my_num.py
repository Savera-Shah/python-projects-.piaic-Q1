import random
def guess_the_num():
    
    secret_num= random.randint(0,99)
    guess = int(input("guess the number :"))
    
    while guess != secret_num:
         if guess < secret_num:
             print(" It is too low !")
         else:
             print(" It is too high !")
             
         print( )
    guess = int(input( "\n Guess the new number")) 
g = guess_the_num()            
        
     