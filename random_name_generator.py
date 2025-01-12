import fileinput
import random
import pprint

# Read words
words = []

for line in fileinput.input(encoding="utf-8"):
    line = line.lstrip().rstrip().lower()
    words.append(line)

print(words)

# Create dictionary of chars per index, and word length counts
char_count_per_index_dict = {}
words_length_dict = {}

for word in words:
    for i in range(0, len(word)):
        # Count word lengths
        length = len(word)
        if length not in words_length_dict:
            words_length_dict[length] = 1
        else:
            words_length_dict[length] += 1

        # Add index if needed
        if i not in char_count_per_index_dict:
            char_count_per_index_dict[i] = {}

        # Count chars for the index
        char = word[i]
        if char not in char_count_per_index_dict[i]:
            char_count_per_index_dict[i][char] = 1
        else:
            char_count_per_index_dict[i][char] += 1

# Use random.sample to choose word length and letters
# Create dual lists of chars and frequencies to use with random.sample: https://docs.python.org/3/library/random.html#random.sample
# 
# Ex:
#   {
#     0: 
#         [
#             (['e', 'a', 'i', 'n'], [2, 5, 34, 1])
#         ],
#     1:
#         [
#             (['z', 'y'], [4, 5])
#         ]
#   }
# At index 0 of a word, 'e' appears 2 times, 'a' appears 5 times, 'i' appears 34 times, etc.
# At index 1 of a word, 'z' appears 4 times, 'y' appears 5 times, etc.
index_char_sampling_lists = {}
for i in char_count_per_index_dict.keys():
    chars = list(char_count_per_index_dict[i].keys())
    char_freq = list(char_count_per_index_dict[i].values())

    if i not in index_char_sampling_lists:
        index_char_sampling_lists[i] = None
    index_char_sampling_lists[i] = (chars, char_freq)

# Do the same for word length
word_length_sampling_list = (list(words_length_dict.keys()), list(words_length_dict.values()))

#### Generate a word #####
num_words = 50
names = []
for i in range(1, num_words + 1):
    new_word_length = random.sample(word_length_sampling_list[0], counts=word_length_sampling_list[1], k=1)[0]

    new_word = ""
    for i in range(0, new_word_length):
        new_letter = random.sample(index_char_sampling_lists[i][0], counts=index_char_sampling_lists[i][1], k=1)[0]
        new_word += new_letter
    names.append(new_word.capitalize())


pprint.pprint(names)