
book_inventory = {
    "fiction": 10,
    "non-fiction": 5,
    "mystery": 8
}


removed_genre = book_inventory.pop("mystery", None)

print(f"removed  count: {removed_genre}")
print(f"Updated book inventory: {book_inventory}")
