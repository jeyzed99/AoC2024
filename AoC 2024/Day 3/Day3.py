import re

with open("Day3Input.txt") as f:
    data = f.read()

pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
tokens = re.findall(pattern, data)

enabled = True
total = 0

for token in tokens:
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    else:  # must be a mul(x,y)
        if enabled:
            x, y = map(int, re.findall(r"\d+", token))
            total += x * y

print("Final total:", total)