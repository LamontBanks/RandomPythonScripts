import fileinput
import random
import pprint
import re

# Read words
words = ['Ceithal']
for line in fileinput.input(encoding="utf-8"):
    line = line.lstrip().rstrip().lower()
    words.append(line)

def next_letter_frequency_names(words, num_names = 50):
    # Next-letter frequency
    # Ex:
    # words = ["hello", "there"]
    # { 
    #     'h': {
    #         'e': 2
    #     },
    #     'e': {
    #         'l': 1,
    #         'r': 1,
    #         # etc...
    #     }
    # }
    next_letter_frequency = {}
    first_letter_frequency = {}
    word_length_frequency = {}

    for word in words:
        # Count next-letter frequency for word length == 1
        if len(word) not in word_length_frequency:
            word_length_frequency[len(word)] = 1
        else:
            word_length_frequency[len(word)] += 1

        # Save first letter frequency
        if word[0] not in first_letter_frequency:
            first_letter_frequency[word[0]] = 1
        else:
            first_letter_frequency[word[0]] += 1

        # Count next-letter frequency for single char
        if len(word) == 1:
            if word not in next_letter_frequency:
                next_letter_frequency[word] = {}
        else:
            for i in range(0, len(word) - 2):
                # Count next-letter frequency for word length > 1
                first_letter = word[i]
                second_letter = word[i + 1]

                if first_letter not in next_letter_frequency:
                    next_letter_frequency[first_letter] = {}
                if second_letter not in next_letter_frequency[first_letter]:
                    next_letter_frequency[first_letter][second_letter] = 1
                else:
                    next_letter_frequency[first_letter][second_letter] += 1

    # Create sampling lists
    word_length_sampling_lists = (
        list(word_length_frequency.keys()),
        list(word_length_frequency.values())
    )

    first_letter_sampling_lists = (
        list(first_letter_frequency.keys()),
        list(first_letter_frequency.values())
    )

    next_letter_sampling_lists = {}
    for first_letter in next_letter_frequency:
        next_letter_sampling_lists[first_letter] = (list(next_letter_frequency[first_letter].keys()),
                                                    list(next_letter_frequency[first_letter].values()))

    #### Generate a word #####
    names = set()
    for i in range(1, num_names + 1):
        new_word = ""

        # Pick the needed values based on the recorded frequencies
        new_word_length = random.sample(word_length_sampling_lists[0], counts=word_length_sampling_lists[1], k=1)[0]
        first_letter = random.sample(first_letter_sampling_lists[0], counts=first_letter_sampling_lists[1], k=1)[0]

        # Get first letter
        new_word += first_letter
        curr_letter = first_letter

        # Get remaining letters
        for i in range(new_word_length - 1):
            if curr_letter not in next_letter_sampling_lists:
                break
            next_letter = random.sample(next_letter_sampling_lists[curr_letter][0], counts=next_letter_sampling_lists[curr_letter][1], k=1)[0]

            new_word += next_letter
            curr_letter = next_letter

        names.add(new_word.capitalize())
    
    return list(names)

"""Generate names based on the frequency of letters appearing in each position"""
def letter_position_frequency_names(words, num_names = 50):
    word_length_frequency = {}
    letter_position_frequency = {}

    for word in words:
        # Count next-letter frequency for word length == 1
        if len(word) not in word_length_frequency:
            word_length_frequency[len(word)] = 1
        else:
            word_length_frequency[len(word)] += 1
        
        # Count letter frequency by position
        for i in range(len(word)):
            letter = word[i]
            if i not in letter_position_frequency:
                letter_position_frequency[i] = {}
            if letter not in letter_position_frequency[i]:
                letter_position_frequency[i][letter] = 1
            else:
                letter_position_frequency[i][letter] += 1

    # Create sampling lists
    word_length_sampling_lists = (
        list(word_length_frequency.keys()),
        list(word_length_frequency.values())
    )

    letter_position_sampling_lists = {}
    for i in letter_position_frequency:
        letter_position_sampling_lists[i] = (list(letter_position_frequency[i].keys()),
                                                    list(letter_position_frequency[i].values()))
        
    #### Generate a word #####
    names = set()
    for i in range(1, num_names + 1):
        new_word = ""

        # Pick the needed values based on the recorded frequencies
        new_word_length = random.sample(word_length_sampling_lists[0], counts=word_length_sampling_lists[1], k=1)[0]
    
        for i in range(new_word_length - 1):
            letter_position_sampling_lists[i]
            next_letter = random.sample(letter_position_sampling_lists[i][0], counts=letter_position_sampling_lists[i][1], k=1)[0]

            new_word += next_letter
        names.add(new_word.capitalize())

    return list(names)
        
def remove_bad_names(names):
    # No double-letters
    names = list(filter(lambda name: re.search(r"(\w)\1", name.lower()) == None, names))

    # Need vowels
    names = list(filter(lambda name: re.search(r"[aeiou]", name.lower()), names))

    # At least 7 letters
    names = list(filter(lambda name: re.search(r"\w{7,}", name.lower()), names))

    return names


names = sorted(remove_bad_names(next_letter_frequency_names(words)))

# Print without the quote marks for easy copy-paste
for name in names:
    print(name)