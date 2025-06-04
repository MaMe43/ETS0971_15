# Tuple :-
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
# Tuple Methods

Python has two built-in methods that you can use on tuples.
#  count()

The tuple method is an immutable sequence type in Python. It is used to store a collection of items, 
which can be of mixed data types. Tuples are similar to lists but cannot be modified after creation. 
This immutability makes tuples useful for representing fixed collections of data, such as coordinates, 
database records, or function return values. Tuples also support indexing, slicing, and iteration.

Key Characteristics:
- Immutable: Once created, the elements of a tuple cannot be changed.
- Ordered: Tuples maintain the order of elements.
- Hashable: Tuples can be used as keys in dictionaries if they contain only hashable elements.
- Lightweight: Tuples use less memory compared to lists.

Common Use Cases:
- Returning multiple values from a function.
- Grouping related data together.
- Using as keys in dictionaries or elements in sets.
# index 
The `index()` method is used to find the first occurrence of a specified value in a tuple. It returns the index of the value if it exists; otherwise, it raises a `ValueError`.

Key Characteristics:
- Searches for the specified value in the tuple.
- Returns the zero-based index of the first occurrence.
- Raises an exception if the value is not found.

Syntax:
```python
tuple.index(value, start, end)
```

Parameters:
- `value`: The item to search for.
- `start` (optional): The starting position to search from.
- `end` (optional): The ending position to search up to (exclusive).

