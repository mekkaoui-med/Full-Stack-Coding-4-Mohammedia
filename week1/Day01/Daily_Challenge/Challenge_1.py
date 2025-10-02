number = int(input("give me a number : \n"))
length = int(input("chose an length : \n"))
print(length)
print(number)
multiple_numbers = []
for i in range (1,length + 1) :
    multiple_numbers.append(number * i)
print(multiple_numbers)