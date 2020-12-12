from collections import defaultdict

def solve(input):
  bag = Bag(input)
  device = Adapter(bag.max_adapter_joltage() + 3)
  conn = Connection()
  while bag.has_next_adapter():
    conn.add_adapter(bag.next_adapter())
  conn.add_adapter(device)
  return conn.differentials[1] * conn.differentials[3]

class Bag:
  def __init__(self, input):
    self.adapters = list(sorted(map(lambda i: Adapter(i), input), reverse=True, key=lambda adapter: adapter.joltage))
  
  def max_adapter_joltage(self):
    return max(map(lambda adapter: adapter.joltage, self.adapters))

  def next_adapter(self):
    return self.adapters.pop()

  def has_next_adapter(self):
    return len(self.adapters) > 0

class Adapter:
  def __init__(self, joltage):
    self.joltage = int(joltage)

class Connection:
  def __init__(self):
    self.adapters = [Adapter(0)]
    self.differentials = defaultdict(int)

  def add_adapter(self, adapter:Adapter):
    previous:Adapter = self.adapters[-1]
    diff = adapter.joltage - previous.joltage
    self.differentials[diff] += 1
    self.adapters.append(adapter)
