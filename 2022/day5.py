#!/usr/bin/env python3

from collections import defaultdict
import input, re

class StackReader:
  def __init__(self) -> None:
    self.stacks = defaultdict(list)
  
  def readline(self, line):
    for i in range(1, 10):
      crate = line[4*i - 3]
      if crate != ' ':
        self.stacks[i].insert(0, crate)

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
  def __init__(self, stacks) -> None:
    self.stacks = stacks

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
    for id in sorted(self.stacks):
      top += self.stacks[id][-1]
    return top

if __name__ == '__main__':
  lines = input.as_list()

  stack_reader = StackReader()
  for l in lines[:lines.index('') - 1]:
    stack_reader.readline(l)
  procedures = [ Procedure(p) for p in lines[lines.index('') + 1:] ]

  stacks = SupplyStacks(stack_reader.stacks)

  stacks.rearrange_all(procedures)
  print(stacks.top_crates())
