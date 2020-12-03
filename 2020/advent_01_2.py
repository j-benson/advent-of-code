def solve(input):
  numbers = [ int(n) for n in input ]
  for n in numbers:
    for m in numbers:
      for x in numbers:
        if n == m or n == x or m == x: continue
        if n + m + x == 2020: return n * m * x
  return None
