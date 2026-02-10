def odd_numbers(start, end):
    print("\nODD Numbers : ")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def even_numbers(start, end):
    print("\nEVEN Numbers : ")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def all_numbers(start, end):
    print("\nAll Numbers : ")
    for i in range(start, end + 1):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    start = int(input("Enter 1st Number: "))
    end = int(input("Enter Last Number: "))

    print("We are working inside mod1 only")
    all_numbers(start, end)