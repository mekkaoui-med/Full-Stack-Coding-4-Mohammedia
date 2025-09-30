TF = True

while TF == True:
    word = input("Enter the longest sentence you can without the character A: \n ")
    if "A" in word :
        TF = True
    else:
        TF = False
print("Congratulations! You just set a new longest sentence! Keep it up!")
