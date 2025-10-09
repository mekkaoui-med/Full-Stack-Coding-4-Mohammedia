#Ex 01 : 

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

car_list = cars.split(", ")
print(f"List of manufacturers: {car_list}")

print(f"There are {len(car_list)} manufacturers in the list.\n")

car_list_sorted = sorted(car_list, reverse=True)
print("Manufacturers in reverse (Z-A):")
print(car_list_sorted, "\n")

has_o = [car for car in car_list if 'o' in car.lower()]
print(f"Manufacturers with the letter 'o': {len(has_o)} → {has_o}")

no_i = [car for car in car_list if 'i' not in car.lower()]
print(f"Manufacturers without the letter 'i': {len(no_i)} → {no_i}\n")

print("=== BONUS ===")
cars_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_cars = list(set(cars_with_duplicates))
print(f"Companies without duplicates ({len(unique_cars)} total):")
print(", ".join(unique_cars))

reversed_letters = [car[::-1] for car in sorted(unique_cars)]
print("\nManufacturers in ascending order (A-Z) but with reversed names:")
print(reversed_letters)

#Ex02 : 

def get_full_name(first_name, last_name, middle_name=""):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    middle_name = middle_name.capitalize()

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name

#Ex03 :

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '/'
}

def english_to_morse(text):
    text = text.upper()
    morse_code = " ".join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse_code

def morse_to_english(morse_code):
    morse_to_char = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(morse_to_char.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


# - Test :

# english_text = "Hello world"
# morse_result = english_to_morse(english_text)
# print(f"English: {english_text}")
# print(f"Morse: {morse_result}")

# decoded_text = morse_to_english(morse_result)
# print(f"Decoded: {decoded_text}")


