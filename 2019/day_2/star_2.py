import intcode

with open('input') as data:
  program = data.readline()

for noun in range(99, -1, -1):
  for verb in range(99, -1, -1):
    if intcode.run(program, noun, verb) == 19690720:
      print(f'Match! noun:{noun} verb:{verb}')
      answer = 100 * noun + verb
      print(f'Answer:{answer}')
      exit()