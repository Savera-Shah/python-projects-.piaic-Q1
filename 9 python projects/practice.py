import string
import random

def password_generator():
    pass_length = int(input("Enter the length of the password: "))
    if pass_length < 4:  # Ensure the length is enough to include all types of characters
        print("Password length should be at least 4.")
        return
    
    # Character groups
    s1 = random.choice(string.ascii_lowercase)  # Ensure at least one lowercase letter
    s2 = random.choice(string.ascii_uppercase)  # Ensure at least one uppercase letter
    s3 = random.choice(string.digits)           # Ensure at least one digit
    s4 = random.choice(string.punctuation)      # Ensure at least one special character

    # Combine all groups and fill the remaining length
    s = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(s)
    remaining = [random.choice(s) for _ in range(pass_length - 4)]  # Remaining characters

    # Final password with guaranteed inclusion of all character types
    password = list(s1 + s2 + s3 + s4) + remaining
    random.shuffle(password)

    # Output the password
    print("Generated Password: " + "".join(password))

password_generator()
