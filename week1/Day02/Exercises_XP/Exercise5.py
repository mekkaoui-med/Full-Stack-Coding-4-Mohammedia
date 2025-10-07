import random
def user_number(number):
    if not (1 <= number <= 100):
        print("Please enter a number between 1 and 100.")
        return
    random_number = random.randint(1,100)
    if number == random_number:
        print("you do it !!")
    else :
        print("nice try ")
user_number(55)