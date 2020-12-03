def read_data(data_file):
  with open(data_file) as data:
    lines = data.readlines()
  init_state = lines[0][15:-1]
  rules = [(l[:5], l[9]) for l in lines[2:]]
  return (init_state, rules)

def next_generation(generation):
  number, zero, data = generation

  while data[0:3] != "...":
    data = "." + data
    zero += 1
  while data[-3:] != "...":
    data = data + "."

  data2 = ["." for i in range(0, len(data))]
  for i in range(2, len(data) - 2):
    rule_matched = False
    for rule, outcome in rules:
      if rule == data[i-2:i+3]:
        rule_matched = True
        break
    if rule_matched:  
      data2[i] = outcome
  return (number + 1, zero, "".join(data2))

def value(generation):
  n, zero, data = generation
  value = 0
  for i in range(0, len(data)):
    if data[i] == "#":
      value += i - zero
  return value

def print_generation(generation):
  number, zero, data = generation
  print("{}[{}]: {}".format(number, zero, data))

initial_state, rules = read_data("data.txt")
#       (gen, zero, state)
gen = (0, 0, initial_state)

print_generation(gen)
for i in range(0, 20):
  gen = next_generation(gen)
  print_generation(gen)

print(value(gen))
