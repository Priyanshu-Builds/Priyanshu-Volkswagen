# a sequence of characters and Strings are immutable 
# index : 0. aslo supports -ve indexing
# 0,1,2,3,4 = 5
# -5,-4,-3,-2,-1 : -ve indexing
# str = "Hello";
# print(str[0])
# print(str[-5])
# # print(str[-6]) #IndexError
# print(len(str))

# --------

# sentence = "Lets learn Python"
# for ch in sentence:
#   print(ch)

# String slicing :
# s1 = sentence[0:4]
# print(s1)

# print(sentence)

# s2 = sentence[4:]
# print(s2)

# s3 = sentence[:9]
# print(s3)

# -ve index slicing:
# s1 = sentence[-17: -15]
# print(s1)

# print(len(sentence))

# s2 = sentence[-8:-1]
# print(s2)

# s3 = sentence[:-9]
# print(s3)

# ------------

# Membership Operators

# word = 'Python'
# print('h' in word)
# print('a' in word)

# ch = "a"
# if(ch in word):
#     print(f"{ch} is present in word: {word}")
# else:
#   print(f"{ch} is not present in word: {word}")

# # c = 'h'
# for ch in word:
#   if(ch == 'h'):
#     print(f"{ch} is present in word: {word}")
#   else:
#     print(f"{ch} is not present in word: {word}")

# ------------

# word = "Python"
# ch = "a"
# if(ch not in word):
#   print(f"{ch} is not present in word: {word}")
# else:
#   print(f"{ch} is present in word: {word}")
  
# word2 = "Python is simple language"
# ch = 'simple'
# if(ch in word2):
#   print(f"{ch} is present in sentence: {word2}")
# else:
#   print(f"{ch} is not present in sentense: {word2}")