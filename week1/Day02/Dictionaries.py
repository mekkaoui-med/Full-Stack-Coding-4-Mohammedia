def letter_indexes(word):
    """
    This function takes a word as input and returns a dictionary
    where each letter is a key and its value is a list of all
    the positions (indexes) where that letter appears in the word.
    """

    # Initialize an empty dictionary to store results
    index_dict = {}

    # Loop through each letter in the word with its index
    for index, letter in enumerate(word):
        # If the letter is not yet a key, create it with an empty list
        if letter not in index_dict:
            index_dict[letter] = []
        # Append the current index to the letter’s list
        index_dict[letter].append(index)

    return index_dict


# --- Main Program ---
user_word = input("Enter a word: ").lower().strip()
result = letter_indexes(user_word)
print(result)
