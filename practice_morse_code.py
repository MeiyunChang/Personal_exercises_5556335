import sys

def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",

        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }

    translated_text = ""
    for char in text:
            if char.isalpha():
                translated_text += morse_code_dict[char] + " "
            elif char.isspace():
                translated_text += "/"

    return translated_text.rstrip()

def Translator():
    while True:
        print("Morse translator")
        print ("1. Translator")
        print("2. Exit")
        choice = input("Enter choice (1/2): ")
        
        if choice == "1":
            input_content = input ("Enter content:")
            output_content = morse_translator(input_content)
            print(f"{input_content} in Morse code: {output_content}")

        elif choice == "2":
            print ("Exit from the system")
            break

        else:
            print ("Invaild input, please try again.")

if __name__ == "__main__":
    Translator()

# Test cases
print(
    morse_translator("HELLO WORLD")
)  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(
    morse_translator("Morse Code")
)  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
print(
    morse_translator("Dylan")
)
