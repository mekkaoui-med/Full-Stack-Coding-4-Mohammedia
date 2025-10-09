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
