import solvers.advent_08_1 as advent_08_1
import solvers.advent_08_2 as advent_08_2

input = [
  'nop +0',
  'acc +1',
  'jmp +4',
  'acc +3',
  'jmp -3',
  'acc -99',
  'acc +1',
  'jmp -4',
  'acc +6',
]

def test_1():
  assert advent_08_1.solve(input) == 5

def test_2():
  pass

