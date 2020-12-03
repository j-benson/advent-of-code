import math
import star_1

def contains_adjacent(password):
  value = str(password)
  matches = 0
  for i in range(1, len(value)):
    if value[i-1] == value[i]:
      matches += 1
    else:
      if matches > 0 and matches % 2 == 0:
        return False
      matches = 0
  if matches > 0 and matches % 2 == 0:
    return False
  return True

if __name__ == "__main__":
  possible_passwords = []
  for password in range(128392, 643281 +1):
    if contains_adjacent(password) and star_1.never_decreases(password):
      possible_passwords.append(password)

  print(len(possible_passwords))
