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