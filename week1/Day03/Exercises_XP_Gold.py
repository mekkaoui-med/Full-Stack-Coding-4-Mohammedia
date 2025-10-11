#Ex01:

class Circle:
    def __init__(self,radius = 1.0):
        self.radius = radius
    def perimeter(self):
        P = self.radius * 2 * 3.14
        return P
    def area(self):
        A =3.14 * self.radius * self.radius
        return A
#Ex02 :

class MyList :
    def __init__(self,letters):
        self.letters = letters
    def rev_list(self):
        self.letters.reverse()
        print(self.letters)
    def sort_list(self):
        return sorted(self.letters)

#Ex03 :
class MenuManager : 
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten_index": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten_index": True}
        ]
    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name" : name,
            "price": price,
            "spice_level" : spice,
            "gluten_index" : gluten
        }
        self.menu.append(new_dish)
    
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                if price is not None:
                    dish["price"] = price
                if spice is not None:
                    dish["spice_level"] = spice
                if gluten is not None : 
                    dish["gluten_index"] = gluten
                    print(f"{name} has been updated")
                    return
        print(f"{name} was not fund in the menu")
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name:
                self.menu.remove(dish)
                print(f"{name} has beeen removed from the menu .")
                return
            else:
                pass
        print(f"{name} was not found in the menu.")


# restaurant = MenuManager()

# print("=== Test 1: Initial Menu ===")
# for dish in restaurant.menu:
#     print(dish)

# print("\n=== Test 2: Add Item ===")
# restaurant.add_item("Pizza", 20, "B", True)
# print(any(dish["name"] == "Pizza" for dish in restaurant.menu))  # Should print True

# print("\n=== Test 3: Update Existing Item ===")
# restaurant.update_item("Salad", 22, "C", True)
# for dish in restaurant.menu:
#     if dish["name"].lower() == "salad":
#         print(dish)  # Should show price=22, spice_level='C', gluten_index=True

# print("\n=== Test 4: Update Nonexistent Item ===")
# restaurant.update_item("Pasta", 30, "A", False)  # Should say not found

# print("\n=== Test 5: Remove Existing Item ===")
# restaurant.remove_item("Pizza")
# print(any(dish["name"] == "Pizza" for dish in restaurant.menu))  # Should print False

# print("\n=== Test 6: Remove Nonexistent Item ===")
# restaurant.remove_item("Taco")  # Should say not found

# print("\n=== Test 7: Case Insensitivity ===")
# restaurant.update_item("soup", 12, None, None)
# restaurant.remove_item("hamburger")
# for dish in restaurant.menu:
#     print(dish)

# print("\n=== Final Menu ===")
# for dish in restaurant.menu:
#     print(dish)