# Name: -> Priyanshu
# Program: Command line Shopping List app with file persistence and quantity support

import os

class ShoppingList:

    def __init__(self):
        self.filename = "shopping_list.txt"
        self.items = {} # I have used dictionary so that list stores both items with their quantity if user wants.
        self.load_items()

    def start_menu(self):
        print("\nType item name to add to your shopping list & use the below commands to do operations :=> \n")
        print(">>>>>>>>>>>>>------------------Shopping List Commands------------------<<<<<<<<<<<<<<<")
        print("DONE     → Exit program")
        print("HELP     → Show commands again")
        print("SHOW     → Display shopping list")
        print("REMOVE   → Remove item or quantity")
        print("CLEAR    → Empty the list")
        print("SEARCH   → Find an item")
        print(">>>>>>>>>>>>>----------------------------------------------------------<<<<<<<<<<<<<<<\n")

    def normalize(self, item):
        return item.capitalize()

    def parse_item(self, text):
        parts = text.lower().split("x")
        item = parts[0].strip()

        qty = 1
        if len(parts) > 1:
            try:
                qty = int(parts[1])
            except:
                print("Invalid quantity entered. Setting quantity to 1.")

        return self.normalize(item), qty

    def load_items(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    for line in file:
                        item, qty = line.strip().split(",")
                        self.items[item] = int(qty)
                if self.items:
                    print("Previous shopping list loaded successfully.")
        except:
            print("Error loading file. Starting with empty list as loading failed.")

    def save_items(self):
        try:
            with open(self.filename, "w") as file:
                for item, qty in self.items.items():
                    file.write(f"{item},{qty}\n")
            print("List saved successfully.")
        except:
            print("Error saving file. Something bad happened in the back!!")

    def add_to_list(self, text):
        item, qty = self.parse_item(text)

        if item in self.items:
            self.items[item] += qty
            print(item, "quantity updated.")
        else:
            self.items[item] = qty
            print(item, "added to your shopping list.")

        print("You have", len(self.items), "items on your list.")
        print("Tip -> Type HELP anytime to see available commands.")

    def remove_item(self, text):
        item, qty = self.parse_item(text)

        if item in self.items:
            if self.items[item] > qty:
                self.items[item] -= qty
                print(qty, item, "removed. Remaining:", self.items[item])

            elif self.items[item] == qty:
                del self.items[item]
                print(item, "completely removed from your shopping list.")

            else:
                print("You only have", self.items[item], item, "in the list.")

            print("You have", len(self.items), "items on your list.")
        else:
            print(item, "not found in your shopping list.")

    def search_item(self, word):
        word = word.capitalize()
        found = [item for item in self.items if word in item]

        if found:
            print("Item found:")
            for item in found:
                print("-", item, f"(x{self.items[item]})")
        else:
            print("No matching item found in the list.")

    def show_shopping_list(self):
        print("My Shopping List:")
        if not self.items:
            print("(List is empty)")
        else:
            for item in sorted(self.items):
                print("-", item, f"(x{self.items[item]})")
        print("Total items:", len(self.items))

def main():
    app = ShoppingList()
    app.start_menu()

    try:
        while True:
            user_input = input("> ").strip()

            if user_input.upper() == "DONE":
                print("!!Thanks for using Shopping List App!!")
                app.save_items()
                app.show_shopping_list()
                break

            elif user_input.upper() in ["HELP", "MENU", "COMMAND", "COMMANDS", "?"]:
                app.start_menu()


            elif user_input.upper() == "SHOW":
                app.show_shopping_list()

            elif user_input.upper() == "REMOVE":
                app.show_shopping_list()
                item = input("What do you want to remove: ")
                app.remove_item(item)

            elif user_input.upper() == "CLEAR":
                confirm = input("Are you sure you want to clear the whole list :=> (yes/no): ")
                if confirm.lower() == "yes":
                    app.items.clear()
                    print("Shopping list cleared.")
                else:
                    print("Clear cancelled as per your request.")

            elif user_input.upper() == "SEARCH":
                word = input("Enter item to search from the list: ")
                app.search_item(word)

            else:
                app.add_to_list(user_input)

    except EOFError:
        print("\nEOF received from you so saving and exiting...")
        app.save_items()


if __name__ == '__main__':
    main()