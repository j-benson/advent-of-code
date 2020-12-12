def solve(input, premable=25):
  xmas = Xmas(input, premable)
  while(True):
    value = xmas.next()
    if value not in xmas.valid_values:
      return value
  return None

class Xmas:
  def __init__(self, data, premable):
    self.data = [ int(item) for item in data ]
    self.premable = premable
    self.pointer = premable
    self._calc_past_values()
    self._calc_valid_values()

  def next(self):
    self.pointer += 1
    next_value = self.data[self.pointer]
    self._calc_past_values()
    self._calc_valid_values()
    return next_value

  def _calc_valid_values(self):
    self.valid_values = set()
    for value1 in self.past_values:
      for value2 in self.past_values:
        if value1 != value2:
          self.valid_values.add(value1 + value2)

  def _calc_past_values(self):
    self.past_values = [ self.data[i] for i in range(self.pointer - self.premable, self.pointer) ]
