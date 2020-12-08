import re

f = open('day4-input', 'r')
data = f.read()
f.close()

documents = data.split('\n\n')

def isValidTravelDoc(doc):
  birthYear = re.search(r'byr:([0-9]{4})(\s|$)', doc)
  if birthYear is not None:
    year = int(birthYear.group(1))
    if year < 1920 or year > 2002:
      print('Invalid birth year ')
      return False

  issueYear = re.search(r'iyr:([0-9]{4})(\s|$)', doc)
  if issueYear is not None:
    year = int(issueYear.group(1))
    if year < 2010 or year > 2020:
      print('Invalid issue year')
      return False

  expirationYear = re.search(r'eyr:([0-9]{4})(\s|$)', doc)
  if expirationYear is not None:
    year = int(expirationYear.group(1))
    if year < 2020 or year > 2030:
      print('Invalid expiration year')
      return False

  height = re.search(r'hgt:([0-9]+)(cm|in)(\s|$)', doc)
  if height is not None:
    value = int(height.group(1))
    unit = height.group(2)

    if unit == 'cm':
      if value < 150 or value > 193:
        print('Invalid height centimeters')
        return False
    elif unit == 'in':
      if value < 59 or value > 76:
        print('Invalid height inches')
        return False

  hairColor = re.search(r'hcl:#[0-9a-f]{6}(\s|$)', doc)
  eyeColor = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)', doc)
  passportId = re.search(r'pid:\d{9}(\s|$)', doc)
  countryId = re.search(r'cid:\S+(\s|$)', doc)

  fields = [birthYear, issueYear, expirationYear, height, hairColor, eyeColor, passportId, countryId]

  field_count = sum(v is not None for v in fields)

  if field_count == 8 or (field_count == 7 and countryId is None):
    return True
  else:
    print('Missing field')
    return False


valid_docs = 0
for doc in documents:
  if isValidTravelDoc(doc):
    print('Valid!')
    valid_docs += 1

  print(doc)
  print('')

print(valid_docs)
