#Ex01 : 

birthdays = {
    "Ayoub": "1998/04/12",
    "Salma": "2001/09/23",
    "Youssef": "1995/12/07",
    "Khadija": "1988/03/30",
    "Rayan": "2003/06/15"
}


print("Welcome to the Birthday Dictionary!")
print("You can look up the birthdays of the people in the list!")

print("\nHere are the people you can search for:")
for name in birthdays:
    print("-", name)

person = input("\nWhose birthday do you want to look up? ").capitalize()
print(person)

if person in birthdays:
    print(f"{person}'s birthday is on {birthdays[person]}.")


#Ex02 : 

birthdays = {
    "Ayoub": "1998/04/12",
    "Salma": "2001/09/23",
    "Youssef": "1995/12/07",
    "Khadija": "1988/03/30",
    "Rayan": "2003/06/15"
}


print("Welcome! You can look up the birthdays of the people in the list!\n")
print("Here are the people we have birthdays for:")

for name in birthdays:
    print(f"- {name}")

user_input = input("\nEnter a name to find their birthday: ").capitalize()

if user_input in birthdays:
    print(f"{user_input}'s birthday is {birthdays[user_input]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {user_input}.")

#Ex03 : 

def sum(x):
    x_str = str(x)
    total = int(x_str) + int(x_str * 2) + int(x_str * 3) + int(x_str * 4)
    return total

#Ex04: 

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        count += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            break
    return count

def main():
    results = []  

    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)

    total_throws = sum(results)
    average_throws = total_throws / len(results)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()
