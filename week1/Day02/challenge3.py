User_dictionary = {}
while True:
   key = input("Enter the key: ")
   if key.lower() == "quit":
       break
   value = input("Enter the value: ")
   if value.lower() == "quit":
       break
   User_dictionary[key] = value 
print(User_dictionary)