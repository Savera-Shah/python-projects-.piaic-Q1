import string
import random

def password_generator():
     print(" ... PASSWORD GENERATOR ...\n")
     pass_lenght= int(input("Enter the lenght of password : "))
        
     s1= string.ascii_lowercase
    # print(s1)
     s2= string.ascii_uppercase
    # print(s1)
     s3= string.digits
    # print(s1)
     s4= string.punctuation
    # print(s1)
    
     s=[]
     s.extend(list(s1))
     s.extend(list(s2))
     s.extend(list(s3))
     s.extend(list(s4))
    
     random.shuffle(s)

     print ("Genetrated password : ", " ".join(s[0:pass_lenght]))
        
password_generator()    