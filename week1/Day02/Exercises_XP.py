#Ex01:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))

print(my_dict)

#Ex02:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name} has to pay ${price}")
    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

#Ex03 :

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
# print(brand)
print(f"Zara's clients are : {','.join(brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
# print(brand)
del brand["creation_date"]
# print(brand)
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
for key in brand:
    print(key)

# #or
# print(brand.keys())
more_on_zara = {
    "creation_date" :1975,
    "number_stores" : 10000
}
# print(more_on_zara)
brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])

#what_happend ="The update() method replaces existing keys with the new values from more_on_zara.That’s why number_stores changed from 2 to 10000."

#Ex04:

def describe_city(city,country= "maroc") :
    print(f"{city} is in {country}")
describe_city("rabat")

#Ex05:

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

#Ex06:

def make_shirt(size = "Large",text = "I love Python"):
    print(f"the size of the shirt is {size} and the text is '{text} '")
make_shirt("large","hello world")
make_shirt()
make_shirt("Small","One code , code One ")
make_shirt("medium","Hi it's me")

#Ex07 :

import random
def get_random_temp(season):
    match season :
        case t if t == "winter":
            Temp_random = round(random.uniform(-10,16), 2)
        case t if t == "spring" : 
            Temp_random = round(random.uniform(10,24), 2)
        case t if t == "summer" :
            Temp_random = round(random.uniform(20,32), 2)
        case t if t == "autumn" :
            Temp_random = round(random.uniform(15,25), 2)
        
    # print(Temp_random)
    return Temp_random
# get_random_temp("winter")

name_season = input("type in a season: \n").lower()

def main():

    random_temp = get_random_temp(name_season)    
    print(f"Hi temperature right now is {random_temp} degrees Celsius.")
    match random_temp :
        case t if t < 0 :
            print("Brrr, that’s freezing! Wear some extra layers today")
        case t if 0 <= t < 16 :
            print("Quite chilly! Don’t forget your coat")
        case t if 16 <= t < 23 :
            print("The weather is perfect not too hot, not too cold. Enjoy your day!")
        case t if 23 <= t < 32 :
            print("It's warm and sunny , perfect beach weather! Don't forget sunscreen")
        case t if 32 <= t < 40 :
            print("It's extremely hot, stay in the shade and drink lots of water!")
        

main()

#Ex08 : 
# Star Wars Quiz

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]


def ask_questions(data):
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        print("\n" + item["question"])
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers


def show_results(correct, incorrect, wrong_answers):
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if wrong_answers:
        print("\nYou got these wrong:")
        for w in wrong_answers:
            print(f"\nQuestion: {w['question']}")
            print(f"Your answer: {w['your_answer']}")
            print(f"Correct answer: {w['correct_answer']}")

    if incorrect > 3:
        play_again = input("\nYou had more than 3 wrong answers . Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            print("\nLet's try again!\n")
            main()
        else:
            print("Thanks for playing! May the Force be with you ")


def main():
    correct, incorrect, wrong_answers = ask_questions(data)
    show_results(correct, incorrect, wrong_answers)


main()