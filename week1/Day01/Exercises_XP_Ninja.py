#Ex01:

"""
>>> 3 <= 3 < 9 ----> True.
>>> 3 == 3 == 3----> True.
>>> bool(0) ---->false.
>>> bool(5 == "5") ----> false.
>>> bool(4 == 4) == bool("4" == "4") ----> True.
>>> bool(bool(None)) ----> false.

>>>

[
    x = (1 == True)
    y = (1 == False)
    a = True + 4
    b = False + 10
]

    X = true.
    Y = false.
    a = 5.
    b = 10

"""
#ex02:

TF = True

while TF == True:
    word = input("Enter the longest sentence you can without the character A: \n ")
    if "A" in word :
        TF = True
    else:
        TF = False
print("Congratulations! You just set a new longest sentence! Keep it up!")

#Ex03 :

import re

My_Paragraph = "The golden sun dipped below the horizon, casting a warm glow over the quiet city streets. Shadows stretched long, and the air was filled with the soft hum of evening life. Somewhere in the distance, a lone violinist played a haunting melody that seemed to speak directly to the heart. It was in these fleeting moments, where time felt suspended, that one could truly notice the small wonders of the world: the way the wind whispered through the trees, the laughter of children fading into the night, and the gentle sparkle of lights reflecting on rain-soaked cobblestones. Life, in all its chaos, still held moments of breathtaking beauty — if only one took the time to see."
num_characters = len(My_Paragraph)
print(num_characters)
sentences = re.split(r'[.!?]', My_Paragraph)
num_sentences = len(sentences)
#print(sentences)
print(num_sentences)
words = re.findall(r"\b\w+\b", My_Paragraph.lower())
num_words = len(words)
#print(words)
print(num_words)
unique_words = set(words)
num_unique_words = len(unique_words)
print(unique_words)
