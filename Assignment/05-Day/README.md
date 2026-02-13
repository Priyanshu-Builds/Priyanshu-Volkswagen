# Shopping List Command Line App

**Done By:** Priyanshu  

This is a Python console application that manages a persistent shopping list.  
The program allows users to **add, remove, search, and store items** in a text file so the list remains saved between program runs.

---

## Features Implemented

### Required Features
- Interactive command menu  
- Add, remove, and show shopping list  
- File persistence using **shopping_list.txt**  
- Case-insensitive commands  
- Item normalization (Capitalized format)  
- Duplicate prevention  
- Graceful EOF handling (**Ctrl + D / Ctrl + Z**)  

---

### Extra Features (Enhancements)
- **CLEAR command** to empty list after confirmation  
- **SEARCH command** to find items by name  
- **Alphabetical sorting** when displaying the list  
- **Quantity support**
  - Example: `Milk x2`
- **Partial quantity removal**
  - Example: remove `Milk x2` from `Milk x4`
- Multiple help commands supported:
  - `HELP`, `MENU`, `COMMAND`, `COMMANDS`, `?`

---

## How to Run

Open terminal in the project folder and run:

```bash
python shopping_list.py