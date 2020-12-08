f = open("day1-input", "r")
numbers = []
for line in f:
  numbers.append(int(line))


for x in numbers:
  for y in numbers:
    if x == 1010 and y == 1010:
      print("problem!")

    if x == y:
      continue

    if x + y == 2020:
      print(x)
      print(y)
      print(x * y)
