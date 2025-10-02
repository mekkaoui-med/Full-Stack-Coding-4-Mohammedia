User_word = input("Enter a word : \n")
new_word = []
for i in range(len(User_word)):
    if i == 0 or User_word[i] != User_word[i - 1]:
        # new_word += User_word[i]
        new_word.append(User_word[i])
result = "".join(new_word)

print(result)