def translate(text):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in text:
        if ch.isalpha() and ch not in vowels:
            result += ch + "o" + ch
        else:
            result += ch

    return result

text = input("Enter text to translate: ")
print("Translated text:", translate(text))