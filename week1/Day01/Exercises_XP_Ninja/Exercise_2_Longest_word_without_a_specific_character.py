TF = True

while TF == True:
    word = input("Enter the longest sentence you can without the character A: \n ")
    for letter in word:
        if letter == "A":
            TF = True
            break
        else:
            TF = False
print("Congratulations! You just set a new longest sentence! Keep it up!")
