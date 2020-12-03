from datetime import datetime

def remove_all_from_polymer(polymer, type):
  p = polymer
  p = p.replace(type.lower(), "")
  p = p.replace(type.upper(), "")
  return p

def react_polymer(polymer):
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
  polymer_length = len(polymer)
  print("length: {}".format(polymer_length))
  return polymer_length


def will_react(p1, p2):
  return p1.lower() == p2.lower() and p1 != p2

def remove_from_polymer(polymer, i):
  return polymer[:i] + polymer[i+2:]

if __name__ == "__main__":
    with open('../data.txt') as data:
      polymer = data.read()

    polymer_trials = [
      ('a', react_polymer(remove_all_from_polymer(polymer, 'a'))),
      ('b', react_polymer(remove_all_from_polymer(polymer, 'b'))),
      ('c', react_polymer(remove_all_from_polymer(polymer, 'c'))),
      ('d', react_polymer(remove_all_from_polymer(polymer, 'd'))),
    ]
    
    print(polymer_trials)