from solvers.advent_09_1 import Xmas

def solve(input, premable=25, weakness=257342611):
  xmas = Xmas(input, premable)
  contiguous = find_weak_contiguous(xmas, weakness)
  return min(contiguous) + max(contiguous)

def find_weak_contiguous(xmas, weakness):
  try:
    while(True):
      xmas.next()
      past_values = list(xmas.past_values)
      while len(past_values) > 1:
        if sum(past_values) == weakness:
          return past_values
        else:
          past_values.pop(0)
  except:
    pass
  return None
