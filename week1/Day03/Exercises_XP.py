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

sarahs_dog = Dog("Teacup",20)
print(f"sarahs_dog name is : {sarahs_dog.name}")
print(f"sarahs can jump {sarahs_dog.height} cm")

sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height < davids_dog.height:
    print(f"{davids_dog.name} is bigger")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger")
else :
    pass

#Ex03 : 
#
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Ex04