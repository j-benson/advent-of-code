from day5 import StackReader, SupplyStacks, Procedure

def test_stack_reader():
  r = StackReader()
  r.readline('            [J] [Z] [G]            ')
  r.readline('[S] [S] [B] [D] [F] [L] [Z] [N] [L]')
  assert [ 'S' ] == r.stacks[1]
  assert [ 'S' ] == r.stacks[2]
  assert [ 'D', 'J' ] == r.stacks[4]
  assert [ 'L', 'G' ] == r.stacks[6]
  assert [ 'L' ] == r.stacks[9]

def test_supply_stack():
  stacks = SupplyStacks({
    1: [ 'Z', 'N' ],
    2: [ 'M', 'C', 'D' ],
    3: [ 'P' ]
  })

  stacks.rearrange(Procedure('move 1 from 2 to 1'))
  assert [ 'Z', 'N', 'D' ] == stacks[1]
  assert [ 'M', 'C' ] == stacks[2]
  assert [ 'P' ] == stacks[3]

  stacks.rearrange(Procedure('move 3 from 1 to 3'))
  assert [ ] == stacks[1]
  assert [ 'M', 'C' ] == stacks[2]
  assert [ 'P', 'Z', 'N', 'D' ] == stacks[3]

  stacks.rearrange(Procedure('move 2 from 2 to 1'))
  assert [ 'M', 'C' ] == stacks[1]
  assert [ ] == stacks[2]
  assert [ 'P', 'Z', 'N', 'D' ] == stacks[3]

  stacks.rearrange(Procedure('move 1 from 1 to 2'))
  assert [ 'M' ] == stacks[1]
  assert [ 'C' ] == stacks[2]
  assert [ 'P', 'Z', 'N', 'D' ] == stacks[3]

  assert 'MCD' == stacks.top_crates()

def test_procedure():
  procedure = Procedure('move 1 from 2 to 3')
  assert 1 == procedure.move_crates
  assert 2 == procedure.from_stack
  assert 3 == procedure.to_stack
