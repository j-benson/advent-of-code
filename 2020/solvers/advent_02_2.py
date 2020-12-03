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

    c1 = password[min_char - 1] == char
    c2 = password[max_char - 1] == char

    if c1 ^ c2: valid += 1

  return valid
