a = ["aa", "bb", "cc"]
b = ["dd", "ee", "ff"]

for index, item in enumerate(a):
    print(index)
    print(item)

for x, y in zip(a, b):
    print(f"x = {x}, y = {y}")
