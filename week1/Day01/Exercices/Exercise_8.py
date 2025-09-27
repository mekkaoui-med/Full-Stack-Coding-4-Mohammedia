sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
target = "Pastrami sandwich"
while target in sandwich_orders:
    sandwich_orders.remove(target)
#print(sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print("I made your ",current_sandwich)
