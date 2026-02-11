def filter_long_words(words, length):
    result = []
    for word in words:
        if len(word) > length:
            result.append(word)
    return result

n = int(input("How many words do you want to enter? => "))
words = []

for i in range(n):
    words.append(input(f"Enter word {i+1}: "))

length = int(input("Enter the length to filter words: "))

print("Words longer than given length are:", filter_long_words(words, length))