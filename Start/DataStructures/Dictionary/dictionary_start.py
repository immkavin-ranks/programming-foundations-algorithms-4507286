# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage

# speed
# unordered


# TODO: create a dictionary all at once
items1 = dict({"key1": 1, "key2": 2, "key3": 3})

print(items1)
# TODO: create a dictionary progressively
items2 = {}
items2["key2"] = 1
items2["key4"] = 5
items2["key3"] = 3
print(items2)


# TODO: replace an item
items2["key4"] = 5
print(items2)

# TODO: try to access a nonexistent key
# print(items1["key"])

# TODO: iterate the keys and values in the dictionary
for key, item in items2.items():
    print("key:", key, "value:", item)