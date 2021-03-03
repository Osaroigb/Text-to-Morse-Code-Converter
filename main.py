# Dictionary containing all characters and its morse code
morse_codes = {"a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.", "h": "....",
               "i": "..", "j": ".___", "k": "_._", "l": "._..", "m": "__", "n": "_.", "o": "___", "p": ".__.",
               "q": "__._", "r": "._.", "s": "...", "t": "_", "u": ".._", "v": "..._", "w": ".__", "x": "_.._",
               "y": "_.__", "z": "__..", "1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....",
               "6": "_....", "7": "__...", "8": "___..", "9": "____.", "0": "_____", ",": "__..__", "?": "..__..",
               ":": "___...", "-": "_...._", '"': "._.._.", "(": "_.__.", "=": "_..._", ".": "._._._", "/": "_.._.",
               "'": ".____.", ")": "_.__._", "+": "._._.", "@": ".__._."}


def morse(msg):
    """A function that converts a string of text into morse code"""

    word_list = msg.split()
    morse_text = ""

    # if the text is one word or one letter
    if len(word_list) == 1:

        numb = 0
        text_str = word_list[0]

        for letter in text_str:

            numb += 1

            if numb == len(text_str):
                morse_text += morse_codes[letter]
            else:
                morse_text = morse_text + morse_codes[letter] + " "

        print()
        print(morse_text)
    # if the text is an empty string
    elif len(word_list) == 0:

        print()
        print("You didn't type anything. Try again!")
    # if the text contains multiple words
    else:

        word_count = 0  # to keep count of each word in the list of words

        for word in word_list:

            word_count += 1

            if len(word) > 1:

                char_count = 0  # to keep count of each character in a word

                for char in word:

                    char_count += 1

                    if len(word) == char_count and word == word_list[-1:][0]:
                        morse_text += morse_codes[char]
                    elif len(word) == char_count:
                        morse_text = morse_text + morse_codes[char] + " / "
                    else:
                        morse_text = morse_text + morse_codes[char] + " "
            # for single characters in the word_list
            else:

                if len(word_list) == word_count:
                    morse_text += morse_codes[word]
                else:
                    morse_text = morse_text + morse_codes[word] + " / "

        print()
        print(morse_text)


# ask the user for a text input and convert to lowercase
text = input("What text do you want to convert? ").lower()
# convert the text input by the user into morse code
morse(text)
