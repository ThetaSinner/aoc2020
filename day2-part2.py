import re

def isPass(test):
  pattern = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
  search_result = re.search(pattern, test)
  if search_result is None:
    print('No match: ' + test)
    return False

  min = int(search_result.group(1))
  max = int(search_result.group(2))

  char = search_result.group(3)
  password = search_result.group(4)

  char1 = password[min - 1]
  char2 = password[max - 1]

  return (char1 == char and char2 != char) or (char1 != char and char2 == char)


valid_passwords = 0
f = open("day2-input", "r")
numbers = []
for line in f:
  if isPass(line):
    valid_passwords += 1

print(valid_passwords)
