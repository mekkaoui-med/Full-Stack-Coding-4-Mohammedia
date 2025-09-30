User_name = input("hi can you tell me your name ")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
if User_name in names:
    print("the first occurence is at index:", names.index(User_name))
else:
    print("name not found in the list")