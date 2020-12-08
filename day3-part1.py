f = open("day3-input", "r")

lines = []
for line in f:
  lines.append(line.strip())

f.close()

incr_x = 3
incr_y = 1

pos_x = 0
pos_y = 0

steps = 0

trees = 0
while steps < len(lines):
  char = lines[pos_y][pos_x % len(lines[0])]

  if char == '#':
    trees += 1

  pos_x += incr_x
  pos_y += incr_y
  steps += 1

print(trees)
