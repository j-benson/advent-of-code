
def solve(input):
  return max(map(lambda i: BoardingPass(i).seat_id, input))

class BoardingPass:
  def __init__(self, data, row_count=128, column_count=8):
    self.row = self._search(
      data = data[:7],
      low_char='F',
      high_char='B',
      i=0,
      min_value=0,
      max_value=row_count
    )
    self.column = self._search(
      data = data[7:],
      low_char='L',
      high_char='R',
      i=0,
      min_value=0,
      max_value=column_count
    )
    self.seat_id = (self.row * 8) + self.column

  def _search(self, data, low_char, high_char, i, min_value, max_value):
    if i == len(data) - 1:
      assert max_value - min_value == 2
      if data[i] == low_char:
        return min_value
      elif data[i] == high_char:
        return max_value - 1
      else:
        raise Exception(f'Expected {low_char} or {high_char} got {data[i]}')
    
    mid_value = int((max_value - min_value) / 2) + min_value
    if data[i] == low_char:
      return self._search(data, low_char, high_char, i + 1, min_value, mid_value)
    elif data[i] == high_char:
      return self._search(data, low_char, high_char, i + 1, mid_value, max_value)
    else:
      raise Exception(f'Expected {low_char} or {high_char} got {data[i]}')