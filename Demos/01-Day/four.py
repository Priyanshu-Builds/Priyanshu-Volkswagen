data = [10, 20, 30, 40, 50] # Iterable : collection

# Iteration : loop
# Iterator : object

# for ele in data:
#   print(ele)

# print(dir(data))

# x = data.__iter__()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# iter_object = iter(data)
# for item in iter_object:
#   print(item)
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))


# def my_for_loop(iterable):
#   iterator = iter(iterable)
#   try:
#     while True:
#       print(next(iterator))
#   except StopIteration:
#     pass
  
# my_for_loop(data)
 
# import sys 
  
# lst = [1,2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'abcdefg'] # growable
# print("List: ", sys.getsizeof(lst))

# iter_obj = iter(lst)
# print("iter : ", sys.getsizeof(iter_obj)) # 48
# # prev index, current value , ref