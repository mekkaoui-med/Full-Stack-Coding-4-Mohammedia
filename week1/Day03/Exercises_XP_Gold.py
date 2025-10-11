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
