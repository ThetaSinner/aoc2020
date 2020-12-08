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
      item_list.append((matches.group(1), matches.group(2)))

    bag_rules.append((container.strip(), item_list))
  else:
    matches = re.search(r'(\d+) (\w+ \w+)', contents)
    bag_rules.append((container.strip(), [(matches.group(1), matches.group(2))]))

f.close()

def contents_can_be(contents, search):
  for item in contents:
    if item[1] == search:
      return True

  return False


def find_all_parents(item, found_container_bags, _bag_rules):
  container_bags = set()

  for rule in _bag_rules:
    if contents_can_be(rule[1], item):
      container_bags.add(rule[0])

  search_container_bags = set([x for x in container_bags])
  for parent in container_bags:
    if parent not in found_container_bags:
      ancestors = find_all_parents(parent, container_bags, _bag_rules)
      search_container_bags = search_container_bags.union(ancestors)

  return search_container_bags


parents = find_all_parents('shiny gold', set(), bag_rules)
print(len(parents))
