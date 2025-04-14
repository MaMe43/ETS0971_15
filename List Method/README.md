# append()
used for adding one item or element at the end of the list . it only takes one item at a time . it has a syntax list_name.append(item)
# clear ()
it is used to remove all elements from the list. it has a syntax list_name.clear()
this method doesn't delete the list completely but it empities it .
# copy() 
it returns a copy of a list . used to make a new copy of a list . it copies the elements of original list but not the reference . it has a syntax new_list = old_list.copy()
# count()
used to identify how many times a specified element appears in the list . simply it returns the number of elements with the specified value .it has a syntax list_name.count(value)
# extend 
used to add all elements from another list to to the end of the current list . it adds each element on by one not as a single item . it has a syntax list1.extend(list2).
# index ()
this method returns the index of the first element with the specified value. it tells the position  of the first occurrence of a specified value in a list.it has  a syntax list_name.index(value,start,end)
# insert()
this method allows  to add an item at a specific index in a list. it Adds an element at the specified position . it has a syntax list_name.insert(index, value)
here index represents The position in the list where we want to insert the item (the first position is 0). value represents The item you want to insert.
# pop()
this method is used to remove and return an item from a list at a specific index. If no index is provided, it removes and returns the last item in the list. simply it adds an element at the specified position . it has a syntax list_name.pop(index)
# remove ()
this method is used to remove the first occurrence of a specified value from a list.
it will only remove the first matching item it finds. if the item is not found, it raises a ValueError.it has a syntax list_name.remove(value)
value represents the item we want to remove .
# reverse ()
this method is used to reverse the order of the items in a list, meaning it modifies the list in-place.it has a syntax list_name.reverse()
# sort ()
this method is used to sort the items of a list in ascending (by default) or descending order. It modifies the original list in place, meaning it changes the order of elements directly in the list. it has syntax list_name.sort(reverse=False, key=None)

 
