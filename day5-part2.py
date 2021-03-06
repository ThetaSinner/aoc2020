import math

class BoardingPass:
  _code = ''
  _row = -1
  _col = -1
  _id = ''

  def __init__(self, code):
    self._code = code
    self._solve()

  def _solve(self):
    row_low = 0
    row_high = 127
    for i in range(0, 7):
      if self._code[i] == 'F':
        row_high = row_low + math.floor((row_high - row_low) / 2)
      elif self._code[i] == 'B':
        row_low = row_low + math.ceil((row_high - row_low) / 2)
      else:
        raise SyntaxError('Invalid row string')

    assert row_low == row_high

    self._row = row_low

    col_low = 0
    col_high = 7
    for i in range(7, 10):
      if self._code[i] == 'L':
        col_high = col_low + math.floor((col_high - col_low) / 2)
      elif self._code[i] == 'R':
        col_low = col_low + math.ceil((col_high - col_low) / 2)
      else:
        raise SyntaxError('Invalid col string')

    assert col_low == col_high

    self._col = col_low

    self._id = self._row * 8 + self._col

  def get_id(self):
    return self._id


bp = BoardingPass('FBFBBFFRLR')

f = open("day5-input", "r")
passes = []
for line in f:
  passes.append(BoardingPass(line))

max_id_pass = max(passes, key=lambda p: p.get_id())
max_id = max_id_pass.get_id()
print('Max pass id', max_id)

min_id_pass = min(passes, key=lambda p: p.get_id())
min_id = min_id_pass.get_id()
print('Min pass id', min_id)

partial_ids = [x.get_id() for x in passes]
complete_ids = set(range(min_id, max_id + 1))

remaining = complete_ids.difference(partial_ids)
assert len(remaining) == 1

boarding_id = list(remaining)[0]
boarding_col = boarding_id % 8
boarding_row = int((boarding_id - boarding_col) / 8)
print("Answer is id =", boarding_id, ' col = ', boarding_col, ' row =', boarding_row)
