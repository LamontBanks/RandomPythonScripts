import fileinput

# Read food
words = []
for line in fileinput.input(encoding="utf-8"):
    line = line.lstrip().rstrip().lower()
    words.append(line)

print(words)