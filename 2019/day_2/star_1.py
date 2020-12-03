# intcode = '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')
with open('input') as data:
  intcode = data.readline().split(',')
intcode = list(map(lambda x: int(x), intcode))


OP_ADD = 1
OP_MULTIPLY = 2
OP_END = 99

opcode_counter = 0
while opcode_counter < len(intcode):
  first = opcode_counter + 1
  second = opcode_counter + 2
  third = opcode_counter + 3

  opcode = intcode[opcode_counter]
  
  if opcode == OP_ADD:
    intcode[intcode[third]] = intcode[intcode[first]] + intcode[intcode[second]]
  if opcode == OP_MULTIPLY:
    intcode[intcode[third]] = intcode[intcode[first]] * intcode[intcode[second]]
  if opcode == OP_END:
    break

  opcode_counter += 4

print(','.join(map(lambda x: str(x), intcode)))