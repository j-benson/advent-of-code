#!/usr/bin/env python3

import input, re

class Procedure:
  pattern = re.compile('move ([0-9]+) from ([0-9]) to ([0-9])')

  def __init__(self, procedure) -> None:
    match = self.pattern.search(procedure)
    if not match:
      raise Exception(f'malformed procedure: {procedure}')
    self.move_crates = int(match.group(1))
    self.from_stack = int(match.group(2))
    self.to_stack = int(match.group(3))
  
  def __str__(self) -> str:
    return f'Procedure(move_crates={self.move_crates},from_stack={self.from_stack},to_stack={self.to_stack})'

class SupplyStacks:
  def __init__(self) -> None:
    self.stacks = dict()
  
  def set_stack(self, id, crates):
    self.stacks[id] = crates
  
  def __setitem__(self, id, crates) -> None:
    self.set_stack(id, crates)

  def get_stack(self, id):
    return self.stacks[id]
  
  def __getitem__(self, id):
    return self.get_stack(id)
  
  def rearrange_all(self, procedures):
    for p in procedures:
      self.rearrange(p)

  def rearrange(self, procedure: Procedure):
    load = self.stacks[procedure.from_stack][-procedure.move_crates:]
    self.stacks[procedure.from_stack] = self.stacks[procedure.from_stack][:-procedure.move_crates]
    for crate in load:
      self.stacks[procedure.to_stack].append(crate)

  def top_crates(self):
    top = ''
    for id in self.stacks:
      top += self.stacks[id][-1]
    return top

if __name__ == '__main__':
  lines = input.as_list()
  procedures = [ Procedure(p) for p in lines[lines.index('') + 1:] ]

  stacks = SupplyStacks()
  stacks[1] = [ 'S', 'T', 'H', 'F', 'W', 'R' ]
  stacks[2] = [ 'S', 'G', 'D', 'Q', 'W' ]
  stacks[3] = [ 'B', 'T', 'W'  ]
  stacks[4] = [ 'D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'  ]
  stacks[5] = [ 'F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z' ]
  stacks[6] = [ 'L', 'P', 'T', 'C', 'V', 'B', 'S', 'G' ]
  stacks[7] = [ 'Z', 'B', 'R', 'T', 'W', 'G', 'P' ]
  stacks[8] = [ 'N', 'G', 'M', 'T', 'C', 'J', 'R' ]
  stacks[9] = [ 'L', 'G', 'B', 'W' ]

  stacks.rearrange_all(procedures)
  print(stacks.top_crates())
