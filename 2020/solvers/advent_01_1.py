def solve(input):
  numbers = [ int(n) for n in input ]
  for n in numbers:
    for m in numbers:
      if n == m: continue
      if n + m == 2020: return n * m
  return None
