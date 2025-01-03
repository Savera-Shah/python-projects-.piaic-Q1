def access(my_list , index):
    try:
        return my_list[int(index)]
    except IndexError:
        return"invalid index"
        
        
def modify(my_list , index , new_index):
    try:
        my_list[index]=int(new_index)
        return my_list
    except IndexError:
        return"Index out of range "
            
def slice_list(my_list, start_index , end_index):
     try:
          return my_list[start_index:end_index]
        
     except(ValueError , IndexError):
          return "Invalid range"    
         
        
def index_game():
    print(f"\n------------------------------------------\n")
    my_list= [10,20,30,40,50]
    print(f"\nInitial list: {my_list}")
    
    
    while True:
        print(f"\n---------welcome to index game-----------")
        print(f"\nInitial list: {my_list}") 
        
        print(f"\nchoose the option :")
        print("1. access list:")
        print("2. modify list:")
        print("3. slice_list ")
        print(f"4. Exit \n")
        choice  = input("enter your choice : ")
        
        if choice  == "1":
            index = input("enter the index to access : ")
            print("Element in index" ,index,"is :  ", access(my_list,index))
        elif choice  == "2":
            index = int(input("enter the index to modify : "))
            if index >= len(my_list) or index< 0:
                print ("enter valid index no")
            else:
                new_value = input("enter the new value: ")
                updated= modify(my_list, index, new_value)
                print(updated)
            
        elif choice  == "3":
            
            start_index =int(input("enter the start index: "))
            end_index= int(input("enter the end index :")) 
            
            print("sliced list: ",slice_list (my_list , start_index , end_index))
        elif choice  == "4":
            print("Good bye! Hope you enjoy the game ")
            break
            
        else:
            print("invalid choice . please select 1 , 2 , 3 or 4 ")
            
               
index_game()    