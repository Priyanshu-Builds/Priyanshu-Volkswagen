# List : indexed collection, [], nexted lists
# numbers = []

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# print(numbers, type(numbers))
# print(numbers[1])
# print(len(numbers))

# ------

# position = [1,2,3,[4,5,6]]
# print(position,len(position))
# print(position[3])
# print(position[3][1])
# print(position[-4])
# print(position[-1][1])
# print(position[-1][-2])

# -------
# slicing :
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[2:6])
# print(numbers[:6])
# print(numbers[6:])
# print(numbers[0:6:2])
# print(numbers[1:6:2])


# -------------

# greetings = ['hello', 'hi', 'hey']
# print(greetings)
# greetings.reverse()
# print(greetings)


# shopping_list = ['bread', 'apple', 'milk', 'banana']
# print(shopping_list)
# shopping_list.sort()
# print(shopping_list)

# shopping_list.sort(reverse=True)
# print(shopping_list)
# new_shopping_list = sorted(shopping_list,reverse=True)
# print(new_shopping_list)

# -------------------

# lst = ['a','b','c', 'd','e','f']
# lst1 = ['j','k']
# print(lst)
# print(lst1)

# lst += lst1
# print(lst)
# lst -= lst1 # TypeError
# print(lst)

# print(len(lst))
# lst[4] ='m'
# print(lst)

# lst.append('m')
# print(lst)

# append method adds nested list in original list
# lst.append(lst1)
# print(lst)

# extend method adds elements in original list expnading its length
# lst.extend(lst1)
# print(lst)


# lst.insert(2,'p')
# print(lst)

# lst.insert(1,lst1)
# print(lst)

# to auto - gerate list items: range()
# lt1 = list(range(5))
# print(lt1)
# lt2 = list(range(1,11,2))
# print(lt2)

# names = ['Peter', 'Tom', 'Jack']
# ages = [55, 20, 34, 67]
 
# zip function emites combination of elements in tuple format. 
# names_ages = zip(names,ages)
# lst3 = list(names_ages)
# print(lst3)

# print(type(names_ages))
# print(names_ages)

# -----


# lst4 = list('hello')
# lst5 = list('World')
# lst4 += lst5
# print(lst4)

# ----
# sentence = 'Python,is,simple, language'
# new_sentence = sentence.split(',')
# print(new_sentence)

#Membership operator:
# courses = ['c++','c','python','javascript','react']
# print('python' in courses)
# print('python' not in courses)

'''
List : Methods
append()
extend()
insert()

remove()
pop()
clear()

index()
count()
reverse()
sort()

del
in/ not in

list()
len()
zip()
'''