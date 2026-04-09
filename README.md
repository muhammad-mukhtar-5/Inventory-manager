# Inventory Manager

A simple command-line Python program for tracking items in a small in-memory inventory.

The script lets you:

- view all inventory items
- add a new item with a quantity
- remove an item by name
- quit the program from the menu

## File

- `inventory-manager.py` - main Python script

## Requirements

- Python 3.x

## How to Run

Open a terminal in this folder and run:

```bash
python inventory-manager.py
```

## Menu Options

When the program starts, it shows this menu:

1. View all items
2. Add an item
3. Remove an item
4. Quit

## How It Works

- The inventory starts as an empty list.
- Each item is stored as a dictionary with:
  - `name`
  - `quantity`
- Added items are appended to the list.
- Removing an item checks names without case sensitivity.
- Viewing items prints each entry in numbered format.

## Example Session

```text
=== Inventory Manager ===
1. View all items
2. Add an item
3. Remove an item
4. Quit
Choose an option: 2
Enter the name of the item to add: Book
specify the quantity: 5
5 Book(s) have been added to the inventory.
```

## Current Behavior Notes

- Inventory data is only stored in memory, so it is lost when the program closes.
- If you choose an invalid menu option, the program prints `invalid option` and exits.
- The quantity input must be a whole number because the script converts it using `int()`.
- If you try to remove an item that does not exist, the program tells you it is not in the inventory.

## Possible Improvements

- save inventory data to a file
- update the quantity of an existing item instead of adding duplicate names
- validate quantity input before converting it to an integer
- keep the program running after an invalid menu choice

