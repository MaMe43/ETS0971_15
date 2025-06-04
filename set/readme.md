# add()
The add() method is used to insert a single element into a set.
Adds the element to the set if it is not already present.
Does nothing if the element is already in the set (no error, no duplicates).
Can only add immutable types (like numbers, strings, tuples).
Mutable types (like lists or other sets) will raise an error.
# clear ()
The clear() method is used to remove all elements from a set.  
After calling clear(), the set will be empty.  
This operation does not take any arguments.  
Useful for resetting a set to its initial empty state.  
# copy()
The copy() method is used to create a shallow copy of a set.  
Returns a new set containing all the elements of the original set.  
The original set remains unchanged.  
Useful for duplicating a set without modifying the original.  
# discard()
The discard() method is used to remove a specific element from a set.  
If the element is present in the set, it will be removed.  
If the element is not present, no error is raised (unlike the remove() method).  
This operation does not return any value.  
Useful for safely removing elements without worrying about their existence in the set.  
# pop()
The pop() method is used to remove and return an arbitrary element from a set.  
If the set is empty, calling pop() will raise a KeyError.  
The specific element removed is not guaranteed, as sets are unordered.  
Useful for retrieving and removing elements when the order does not matter.  