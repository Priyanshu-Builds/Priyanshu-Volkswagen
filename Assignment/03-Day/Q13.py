def find_longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

n = int(input("How many words do you want to enter? =>"))
words = []

for i in range(n):
    words.append(input(f"Enter word {i+1}: "))

print("Length of the longest word is:", find_longest_word(words))