import random
def get_random_temp():
    Temp_random = random.randint(-10,40)
    # print(Temp_random)
    return Temp_random
get_random_temp()

def main():

    random_temp = get_random_temp()
    print(f"Hi temperature right now is {random_temp} degrees Celsius.")
main()