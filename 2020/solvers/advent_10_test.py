import solvers.advent_10_1 as advent_10_1
import solvers.advent_10_2 as advent_10_2
from solvers.advent_10_1 import Bag, Adapter

input = [
  '16',
  '10',
  '15',
  '5',
  '1',
  '11',
  '7',
  '19',
  '6',
  '12',
  '4',
]

input_2 = [
  '28',
  '33',
  '18',
  '42',
  '31',
  '14',
  '46',
  '20',
  '48',
  '47',
  '24',
  '23',
  '49',
  '45',
  '19',
  '38',
  '39',
  '11',
  '1',
  '32',
  '25',
  '35',
  '8',
  '17',
  '7',
  '9',
  '4',
  '2',
  '34',
  '10',
  '3',
]

def test_1():
  assert advent_10_1.solve(input_2) == 220

def test_adapter_order():
  bag = Bag(input_2)
  assert bag.next_adapter().joltage == 1
  assert bag.next_adapter().joltage == 2
  while bag.has_next_adapter():
    last_adapter = bag.next_adapter()
  assert last_adapter.joltage == 49

def test_adapter_max():
  bag = Bag(input_2)
  assert bag.max_adapter_joltage() == 49

def test_adapter_voltages():
  a = Adapter('1')
  assert a.joltage == 1

def test_2_input_1():
  assert advent_10_2.solve(input) == 8

def test_2():
  assert advent_10_2.solve(input_2) == 19208
