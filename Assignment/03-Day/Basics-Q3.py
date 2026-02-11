marks_dict = {}

for i in range(3):
    subject = input(f"Enter subject {i+1} name: ")
    marks = int(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks

print("Marks stored in dictionary:")
print(marks_dict)