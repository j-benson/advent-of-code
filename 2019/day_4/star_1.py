
def contains_adjacent(password):
  value = str(password)
  for i in range(1, len(value)):
    if value[i-1] == value[i]:
      return True
  return False

def never_decreases(password):
  digits = [ int(d) for d in list(str(password)) ]
  for i in range(1, len(digits)):
    if digits[i] < digits[i-1]:
      return False
  return True


if __name__ == "__main__":
  possible_passwords = []
  for password in range(128392, 643281 +1):
    if contains_adjacent(password) and never_decreases(password):
      possible_passwords.append(password)

  print(len(possible_passwords))
