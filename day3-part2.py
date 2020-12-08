f = open("day3-input", "r")

lines = []
for line in f:
  lines.append(line.strip())

f.close()

def countTrees(incr_x, incr_y):
  pos_x = 0
  pos_y = 0

  trees = 0
  while pos_y < len(lines):
    char = lines[pos_y][pos_x % len(lines[0])]

    if char == '#':
      trees += 1

    pos_x += incr_x
    pos_y += incr_y

  return trees

result = countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2)
print(result)
