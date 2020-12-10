import re

program = []

f = open('day8-input')
for line in f:
  program.append(line.strip())

accumulator = 0
program_pointer = 0

executed_instructions = set()

while program_pointer not in executed_instructions:
  instruction_line = program[program_pointer]

  match = re.search(r'(\w{3}) ([\-|+])(\d+)', instruction_line)

  instruction = match.group(1)
  sign = match.group(2)
  value = int(match.group(3))
  if sign == '-':
    value *= -1

  executed_instructions.add(program_pointer)

  if instruction == 'nop':
    program_pointer += 1
  elif instruction == 'jmp':
    program_pointer += value

    if program_pointer < 0 or program_pointer + 1 >= len(program):
      raise IndexError("Out of program bounds")
  elif instruction == 'acc':
    accumulator += value
    program_pointer += 1
  else:
    assert False

print(accumulator)
