import sys


def main():
    word = input("word: ") # returns a string
    print(f"{word = }") # f-string 'formatted'
    # old python
    print("The word is %s." % word) # '%s' is a placeholder for the variable
    # newer python
    print("The word is" + word + ".") # concatenation
    # modern python
    print(f"The word is {word} of length {len(word)}.")
    character_count = dict() # empty dictionary
    for letter in word: # create a variable 'letter'
        print(f"{letter = }")
        # count how many times 'letter' occurs in 'word'
        # save the number in the dictionary
        # use the key to be 'letter'
        character_count[letter] = word.count(letter)
    return 0


if __name__ == '__main__':
    sys.exit(main())