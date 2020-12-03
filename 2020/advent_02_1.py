import re

pattern = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')

def solve(input):
  valid = 0
  for i in input:
    match = pattern.match(i)
    min_char = int(match.group(1))
    max_char = int(match.group(2))
    char = match.group(3)
    password = match.group(4)

    n = 0
    for c in password:
      if c == char: n += 1
    if n >= min_char and n <= max_char: valid += 1

  return valid
