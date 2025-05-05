data = {"name": "Alice", "age": 25}
value = data.setdefault("city", "Unknown")
print(data)
print(value)