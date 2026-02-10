def sample(message):
  print("Here is your msg: {}".format(message))
  
def display():
  # '''This is a display function'''
  """ some code """
  abcd = "something"
  print("""21, Bakers street,
London, 
UK""")

# print(dir(display))
print(display.__doc__)
# print(display.__dir__())
print(display.__module__)

display()

# print(dir())

# -----------------
# sample("10 is greater than 5")

# def test():
#   return "23.33 text value"

# print(test())

# # print(sample("abcd"))
# val = sample("abcd")
# print(val,type(val))