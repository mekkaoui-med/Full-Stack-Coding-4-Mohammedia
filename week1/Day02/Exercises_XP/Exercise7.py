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