f = open("day1-input", "r")
numbers = []
for line in f:
  numbers.append(int(line))


for x in numbers:
  for y in numbers:
    for z in numbers:

      if x == y or x == z or y == z:
        continue

      if x + y + z == 2020:
        print(x)
        print(y)
        print(z)
        print(x * y * z)
