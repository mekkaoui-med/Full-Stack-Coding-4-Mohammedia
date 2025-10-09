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
