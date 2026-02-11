people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("Total number of students:", len(people))

people['Lisa'] = input("Enter new favourite colour for Lisa: ")

people.pop('Jenny')

print("Students sorted alphabetically with colours:")
for name in sorted(people):
    print(name, "->", people[name])