import random


with open("words.txt", "r") as f:
    data = f.read()
word = data.split()

words = random.choice(word)

total_chances = 7
guessed_word= "_"*len(words)
guessed_letter=set()

while total_chances != 0:  
     print(guessed_word)
     letter = input("guess the letter : ").lower()
     
     if not letter.isalpha() or len(letter) != 1:
        print ("incorrect input! please enter a single alphabetic character")
        continue
     
     if letter in guessed_letter:
        print ("You already used this character. Try another one!")
        continue
     
     guessed_letter.add(letter)
     
     if letter in words:
        for index in range(len (words)):
            if words[index]==letter:
                guessed_word= guessed_word[:index]+letter+guessed_word[index +1 :]
                
        if guessed_word == words:
             print("-------------------------------")
             print ("congratulation you win!... \U00002764 \U0001F389 ") 
             print("-------------------------------")
             break      
     else :
         total_chances -=1
         if total_chances == 6:
            print("6 turns left")
            print("---------------")
            print(r"       O      ")
         elif total_chances == 5:
            print("5 turns left")
            print("---------------")
            print(r"      \ O      ")
         elif total_chances == 4:
            print("4 turns left")
            print("---------------")
            print(r"      \ O /     ")
         elif total_chances == 3:
            print("3 turns left")
            print("---------------")
            print(r"      \ O /     ")
            print(r"       /        ")
         elif total_chances == 2:
            print("2 turns left")
            print("---------------")
            print(r"      \ O /     ")
            print(r"       / \      ")
         elif total_chances == 1:
            print("1 turns left")
            print("---------------")
            print(r"      \ O /   <---  ")
            print(r"        |          ")
            print(r"       / \        ")
         elif total_chances == 0:
            print("0 turn left")
            print("---------------")
            print(r"       <------ ")
            print(r"         |      ")
            print(r"  O     / \    ")
            print("-------------------------------")
            
                  
            
else:
    print("-------------------------------")
    print("G_A_M_E  -  O_V_E_R\U0001F494\U0001F494")   
    print("-------------------------------")  
    print("you lose :( \U0001F494 \U0001F622 ")   
    print("-------------------------------")  
    print("ALL THE CHANCES ARE EXHAUSTED ^  ^")
    print("                               __    ")
    print("-------------------------------")
    print("THE CORRECT WORD IS : ", words)
    print("-------------------------------")


    