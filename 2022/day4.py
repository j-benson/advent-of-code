#!/usr/bin/env python3

import input

class AssignmentPair:
  def __init__(self, assignment_pair) -> None:
    self.assignments = [ Assignment(a) for a in assignment_pair.split(',') ]
  
  def _sort_by_size(self) -> set:
    return sorted(self.assignments, key=lambda a: len(a.set), reverse=True)

  def has_full_assignment_overlap(self):
    largest, other = self._sort_by_size()
    return largest.set.issuperset(other.set)
    
class Assignment:
  def __init__(self, assignment) -> None:
    start_id, end_id = assignment.split('-')
    self.set = { int(id) for id in range(int(start_id), int(end_id) + 1) }

  def __len__(self) -> int:
    return len(self.set)

if __name__ == '__main__':
  lines = input.as_list()
  pairs = [ AssignmentPair(l) for l in lines ]
  assigment_overlaps = map(lambda p: 1 if p.has_full_assignment_overlap() else 0, pairs)
  print(sum(assigment_overlaps))
