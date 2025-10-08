
# Challenge-1 : 
number = int(input("give me a number : \n"))
length = int(input("chose an length : \n"))
print(length)
print(number)
multiple_numbers = []
for i in range (1,length + 1) :
    multiple_numbers.append(number * i)
print(multiple_numbers)

# challenge-2 : 
User_word = input("Enter a word : \n")
new_word = []
for i in range(len(User_word)):
    if i == 0 or User_word[i] != User_word[i - 1]:
        # new_word += User_word[i]
        new_word.append(User_word[i])
result = "".join(new_word)

print(result)

#Daily_challenge_GOLD:

from datetime import datetime

birthdate_User = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_User, "%d/%m/%Y")
today = datetime.today()

age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1
print(age)
num_candles = age % 10
is_leap = (birthdate.year % 4 == 0 and birthdate.year % 100 != 0) or (birthdate.year % 400 == 0)

def print_cake(candles):
    candle_line = " " + "i" * candles
    print(f"   ___{candle_line}___")
    print("  |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

if is_leap:
    print("You were born in a leap year! Here are two cakes:")
    print_cake(num_candles)
    print()  
    print_cake(num_candles)
else:
    print_cake(num_candles)

# Exercices :

# Ex01 : 

print(("Python\n") * 4)
# Ex02:

r = pow(99,3) * 8
print(r)

#Ex03:

name = input("Hi!, what is your name ? \n")
my_name = "Mohamed"
if name == my_name :
    print("ooh ! we have the same name!!")
else :
    print("we don't have the same name ")

#Ex04:

user_height = input("can you tell me your height : \n")
if int(user_height) > 145 :
    print("you are tall enough to ride")
else : 
    print("keep growing, you’re getting closer to the fun!")

#Ex05:

my_fav_numbers = {12,54,25,54,58,55,63}
my_fav_numbers.add(100)
my_fav_numbers.remove(63)
friend_fav_numbers = {14,54,88,745,412,21}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

#EX06:

#No, you cannot directly add integers to a tuple because tuples are immutable

#Ex07:

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

apple_count = basket.count("Apples")
print("Number of Apples:", apple_count)

basket.clear()

print(basket)

#Ex08:

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
target = "Pastrami sandwich"
while target in sandwich_orders:
    sandwich_orders.remove(target)
#print(sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print("I made your ",current_sandwich)

#Exercises XP Gold

#Ex01:

month = int(input("Enter a month number (1 to 12): \n"))

if  month in [3,4,5] :
    print("Spring")
elif month in [6,7,8] :
    print("Summer")
elif month in [9,10,11] : 
    print("Autumn")
elif month in [12,1,2] :
    print("Winter")
else : 
    print("Invalid month Please enter a number between 1 and 12")

#Ex02:

print()
for i in range(1,21):
    print(i,end=" ")
print()
print()
new_nbr_list = list(range(1,21))
for i in range(0,len(new_nbr_list),2) :
    print(new_nbr_list[i],end=" ")

#Ex03:

my_name = "Mohamed"
name = ""
while my_name != name :
    name=input("Enter your name:")
print("You entered the correct name!")

#Ex04:

User_name = input("hi can you tell me your name ")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
if User_name in names:
    print("the first occurence is at index:", names.index(User_name))
else:
    print("name not found in the list")

#Ex05:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("Input the 1st number :",num1)
print("Input the 1st number :",num2)
print("Input the 1st number :",num3)
print()


The_Greatest_Number = max(num1,num2,num3)
print("Teh greatest number is : ",The_Greatest_Number)

#Ex06:

import random
print("Try to guess the number between 1 and 9 \n")
    
Lucky_Number = int(input("Enter your Lucky Number:\n"))


Target = random.randint(1,9)
while Lucky_Number != Target:
      print("Better luck this time \n")
      print("-Press '0' anytime to quit-\n")
      if Lucky_Number == 0:
            break
      Lucky_Number = int(input("Enter your Lucky Number:\n"))
if Lucky_Number == Target:
      print("Winner")

#Exercises XP Ninja

#Ex01:

"""
>>> 3 <= 3 < 9 ----> True.
>>> 3 == 3 == 3----> True.
>>> bool(0) ---->false.
>>> bool(5 == "5") ----> false.
>>> bool(4 == 4) == bool("4" == "4") ----> True.
>>> bool(bool(None)) ----> false.

>>>

[
    x = (1 == True)
    y = (1 == False)
    a = True + 4
    b = False + 10
]

    X = true.
    Y = false.
    a = 5.
    b = 10

"""
#ex02:

TF = True

while TF == True:
    word = input("Enter the longest sentence you can without the character A: \n ")
    if "A" in word :
        TF = True
    else:
        TF = False
print("Congratulations! You just set a new longest sentence! Keep it up!")

#Ex03 :

import re

My_Paragraph = "The golden sun dipped below the horizon, casting a warm glow over the quiet city streets. Shadows stretched long, and the air was filled with the soft hum of evening life. Somewhere in the distance, a lone violinist played a haunting melody that seemed to speak directly to the heart. It was in these fleeting moments, where time felt suspended, that one could truly notice the small wonders of the world: the way the wind whispered through the trees, the laughter of children fading into the night, and the gentle sparkle of lights reflecting on rain-soaked cobblestones. Life, in all its chaos, still held moments of breathtaking beauty — if only one took the time to see."
num_characters = len(My_Paragraph)
print(num_characters)
sentences = re.split(r'[.!?]', My_Paragraph)
num_sentences = len(sentences)
#print(sentences)
print(num_sentences)
words = re.findall(r"\b\w+\b", My_Paragraph.lower())
num_words = len(words)
#print(words)
print(num_words)
unique_words = set(words)
num_unique_words = len(unique_words)
print(unique_words)
