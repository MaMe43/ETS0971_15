name = ['mohammed', 'mame', 'yimer']
name2 = ['yimeerr', 'endris']
book = ['novel', 'history', 'science']
book2 = ['fiction', 'literature']
name.extend(name2)
book.extend(book2)
print(name)
print(book)
# the difference between append and extend is that append adds a single element to the end of the list, while extend adds multiple elements from an iterable (like a list) to the end of the list.