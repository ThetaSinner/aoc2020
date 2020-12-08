import re

f = open('day4-input', 'r')
data = f.read()
f.close()

documents = data.split('\n\n')

valid_docs = 0

for doc in documents:
  birthYear = re.search(r'byr:\S+', doc)
  issueYear = re.search(r'iyr:\S+', doc)
  expirationYear = re.search(r'eyr:\S+', doc)
  height = re.search(r'hgt:\S+', doc)
  hairColor = re.search(r'hcl:\S+', doc)
  eyeColor = re.search(r'ecl:\S+', doc)
  passportId = re.search(r'pid:\S+', doc)
  countryId = re.search(r'cid:\S+', doc)

  fields = [birthYear, issueYear, expirationYear, height, hairColor, eyeColor, passportId, countryId]

  field_count = sum(v is not None for v in fields)

  if field_count == 8 or (field_count == 7 and countryId is None):
    valid_docs += 1

print(valid_docs)
