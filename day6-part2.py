def to_set(word):
    return set([char for char in word])


f = open('day6-input')
input = f.read().split('\n\n')

counter = 0
answers = []
for group in input:
  member_answers = group.strip().split('\n')

  member_answer_sets = [to_set(x) for x in member_answers]

  assert len(member_answer_sets) > 0

  overlapping_answers = to_set('abcdefghijklmnopqrstuvwxyz')
  for member_answers in member_answer_sets:
    overlapping_answers = overlapping_answers.intersection(member_answers)

  count = len(overlapping_answers)
  answers.append(count)

print(sum(answers))
