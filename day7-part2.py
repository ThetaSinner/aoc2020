import re

count = 0
bag_rules = []

f = open('day7-input')
for line in f:
  container, contents = line.split('bags contain')

  if 'no other bags' in contents:
    bag_rules.append((container.strip(), []))
  elif ',' in contents:
    content_items = contents.split(',')

    item_list = []
    for item in content_items:
      matches = re.search(r'(\d+) (\w+ \w+)', item)
      item_list.append((int(matches.group(1)), matches.group(2)))

    bag_rules.append((container.strip(), item_list))
  else:
    matches = re.search(r'(\d+) (\w+ \w+)', contents)
    bag_rules.append((container.strip(), [(int(matches.group(1)), matches.group(2))]))

f.close()

def pack_luggage(current_bag, _rules):
  count = 0
  for rule in _rules:
    if rule[0] == current_bag:
      count += sum([next_bag[0] + next_bag[0] * pack_luggage(next_bag[1], _rules) for next_bag in rule[1]])

  return count


print(pack_luggage('shiny gold', bag_rules))
