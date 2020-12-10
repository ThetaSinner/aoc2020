import re

program = []

f = open('day8-input')
for line in f:
  program.append(line.strip())


def execute_program(_program):
  accumulator = 0
  program_pointer = 0

  executed_instructions = set()

  graceful_stop = False

  while not graceful_stop and program_pointer not in executed_instructions:
    line = _program[program_pointer]

    match = re.search(r'(\w{3}) ([\-|+])(\d+)', line)

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

      if program_pointer < 0 or program_pointer > len(_program):
        raise IndexError("Out of program bounds")
      elif program_pointer == len(_program):
        graceful_stop = True
    elif instruction == 'acc':
      accumulator += value
      program_pointer += 1
    else:
      assert False

  return (graceful_stop, accumulator)




for i in range(0, len(program)):
  if 'acc' in program[i]:
    continue

  mod_program = [x for x in program]
  if 'jmp' in mod_program[i]:
    mod_program[i] = mod_program[i].replace('jmp', 'nop')
  elif 'nop' in mod_program[i]:
    mod_program[i] = mod_program[i].replace('nop', 'jmp')
  else:
    assert False

  result = execute_program(mod_program)

  if result[0]:
    print("Clean exit!", i)
    print(result[1])
