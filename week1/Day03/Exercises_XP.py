# # Ex01
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

#EX02 : 
class Dog :
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def bark(self):
        print(f"{self.name} goes woof ")

    def jump(self):
        x = self.height * 2 
        print(f"{self.name} jump {x} cmm hight!")

davids_dog = Dog("Rex",50)
print(f"the dog name is : {davids_dog.name}") 
print(f"the dog hieght is : {davids_dog.height} cmm ")

davids_dog.bark()
davids_dog.jump()