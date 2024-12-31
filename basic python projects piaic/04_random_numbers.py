import random
 
def random_num():
     min_num = 1
     max_num = 100
     n = 0
     for  n in range (10):
        num = random.randint(min_num, max_num)
        n+=1
        print(n , "Random number between 1 to 100 : ", num )
        
random_num()        
     