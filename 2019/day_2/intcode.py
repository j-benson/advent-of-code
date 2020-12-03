
OP_ADD = 1
OP_MULTIPLY = 2
OP_END = 99

def run(program, noun, verb):
  program = [ int(x) for x in program.split(',') ]

  program[1] = noun
  program[2] = verb

  opcode_pointer = 0
  while opcode_pointer < len(program):
    first = opcode_pointer + 1
    second = opcode_pointer + 2
    third = opcode_pointer + 3

    opcode = program[opcode_pointer]
    
    if opcode == OP_ADD:
      program[program[third]] = program[program[first]] + program[program[second]]
    if opcode == OP_MULTIPLY:
      program[program[third]] = program[program[first]] * program[program[second]]
    if opcode == OP_END:
      break

    opcode_pointer += 4

  return program[0]
