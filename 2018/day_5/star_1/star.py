from datetime import datetime

def will_react(p1, p2):
  return p1.lower() == p2.lower() and p1 != p2

def remove_from_polymer(polymer, i):
  return polymer[:i] + polymer[i+2:]


if __name__ == "__main__":
  with open('../data.txt') as data:
    polymer = data.read()

  start_time = datetime.now()
  i = 0
  while i + 1 < len(polymer) - 1:
    if will_react(polymer[i], polymer[i + 1]):
      polymer = remove_from_polymer(polymer, i)
      i = 0
    else:
      i += 1

  end_time = datetime.now()
  time_taken = end_time - start_time
  print("time: {}s".format(time_taken.total_seconds()))

  with open('polymer.txt', 'w') as out:
    out.write(polymer)
  print(len(polymer))