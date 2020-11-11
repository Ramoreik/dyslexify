#!/bin/python
import sys
import random

EXCLUDE_FILTER = ['.', ',', '!','\'','?']

def dislexify(word):
    capitalized = word[0].isupper()
    half = round(len(word) /2)
    word_first_half = []
    word_second_half = []
    word_first_half[:0] = word[:half]
    word_second_half[:0] = word[half:]
    random.shuffle(word_first_half)
    random.shuffle(word_second_half)
    dyslexified = '{}{}'.format(''.join(word_first_half),''.join(word_second_half)) 
    if capitalized:
        dyslexified = dyslexified.capitalize()
    return dyslexified

def filter_line(line):
    symbols = []
    new_line = []
    new_line[0:] = line
    for char in new_line:
        if char in EXCLUDE_FILTER:
            symbols.append([char, new_line.index(char) + len(symbols)])
            new_line.remove(char)
    return {"symbols": symbols, "line": new_line}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
        output = ""
        for line in text.split("\n"):
            filtered = filter_line(line)
            new_line = []
            for word in ''.join(filtered['line']).split(" "):
                if word:
                    new_line.append(dislexify(word))
            new_line[0:] = ' '.join(new_line)
            for symbol in filtered['symbols']:
                new_line.insert(symbol[1], symbol[0])
            output += ''.join(new_line) + "\n"
        print(output)


    else:
        print("Please provide a word.")
        
