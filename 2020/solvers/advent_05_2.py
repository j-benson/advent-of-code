from solvers.advent_05_1 import BoardingPass, Seat, ROW_COUNT, COLUMN_COUNT

def solve(input):
  boarding_passes = set(map(lambda i: BoardingPass(i).seat_id, input))
  plane_seats = Plane().seat_ids
  possible_seats = plane_seats.difference(boarding_passes)
  for s in possible_seats:
    if s + 1 not in possible_seats and s - 1 not in possible_seats:
      return s

class Plane:
  def __init__(self, row_count=ROW_COUNT, column_count=COLUMN_COUNT):
    self.seat_ids = set()
    for r in range(0, row_count):
      for c in range(0, column_count):
        self.seat_ids.add(Seat(r, c).id)

