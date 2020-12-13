from functools import reduce

def solve(input):
  joltages = list(sorted(map(lambda j: int(j), input)))
  num_of_options = []
  for i in range(len(joltages)):
    n = 1
    c = 0
    while True:
      if i+n >= len(joltages): break
      if joltages[i+n] > joltages[i] + 3: break
      c += 1
      n += 1
    if c > 0: num_of_options.append(c)

  return reduce(lambda x, y: x * y, num_of_options)
