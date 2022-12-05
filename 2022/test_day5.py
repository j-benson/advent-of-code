from day5 import SupplyStacks,Procedure

def test_supply_stack():
  stacks = SupplyStacks()
  stacks[1] = [ 'Z', 'N' ]
  stacks[2] = [ 'M', 'C', 'D' ]
  stacks[3] = [ 'P' ]

  stacks.rearrange(Procedure('move 1 from 2 to 1'))
  assert [ 'Z', 'N', 'D' ] == stacks[1]
  assert [ 'M', 'C' ] == stacks[2]
  assert [ 'P' ] == stacks[3]

  stacks.rearrange(Procedure('move 3 from 1 to 3'))
  assert [ ] == stacks[1]
  assert [ 'M', 'C' ] == stacks[2]
  assert [ 'P', 'D', 'N', 'Z' ] == stacks[3]

  stacks.rearrange(Procedure('move 2 from 2 to 1'))
  assert [ 'C', 'M' ] == stacks[1]
  assert [ ] == stacks[2]
  assert [ 'P', 'D', 'N', 'Z' ] == stacks[3]

  stacks.rearrange(Procedure('move 1 from 1 to 2'))
  assert [ 'C' ] == stacks[1]
  assert [ 'M' ] == stacks[2]
  assert [ 'P', 'D', 'N', 'Z' ] == stacks[3]

  assert 'CMZ' == stacks.top_crates()

def test_procedure():
  procedure = Procedure('move 1 from 2 to 3')
  assert 1 == procedure.move_crates
  assert 2 == procedure.from_stack
  assert 3 == procedure.to_stack
