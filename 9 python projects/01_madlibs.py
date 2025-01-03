print(" ...Introduced Yourself... ")

name = input("Please enter your full name : ").strip().title()
age = input("How old are you? : ").strip()
hobby = input("What is one of your favorite hobbies? :  ").strip().capitalize()
goals = input("What are your future goals? (Describe your aspirations or dreams): ").strip()

madlibs = (
    f"Hello everyone!\n"
    f"My name is {name}, and I am {age} years old. "
    f"I have a passion for {hobby}, which brings joy and excitement to my life.\n "
    f"In the future, I aspire to {goals}, and I am determined to work hard to turn this dream into reality.\n "
    f"Thank you for giving me the opportunity to introduce myself!"
)
print(" \n...Your Introduction...\n")

print(madlibs)