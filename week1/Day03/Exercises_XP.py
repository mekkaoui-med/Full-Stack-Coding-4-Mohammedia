# Ex01
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("nana", 4)
cat2 = Cat("lodgy", 2)
cat3 = Cat("tom", 5)


def find_old(cats):
    oldest = max(cats, key=lambda cat: cat.age)
    return oldest


oldest_cat = find_old([cat1, cat2, cat3])
print(f"The oldest cat is: {oldest_cat.name}, and is {oldest_cat.age} years lod.")
