import time 
def  timeup():
    my_time= int (input("Enter the time in seconds : "))
    for x in range( my_time , 0 , -1):
        time.sleep(3)
        seconds= int ( x % 60)
        mintus = int (x/60)% 60
        hours = int (x/3600)
        print(f"{hours:02}:{mintus:02}:{seconds:02}")
        
    print("TIME UP!")
timeup()