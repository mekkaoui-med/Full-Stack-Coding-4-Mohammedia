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
 