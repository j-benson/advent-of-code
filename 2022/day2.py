#!/usr/bin/env python3

import input

class Move:
  def __init__(self, value) -> None:
    self.ROCK = 'A'
    self.PAPER = 'B'
    self.SCISSOR = 'C'
    self.WIN = 'Z'
    self.DRAW = 'Y'
    self.LOSE = 'X'
    self.opponent, self.my = value.split(' ')

  def win(self) -> str:
    if self.opponent == self.ROCK:
      return self.PAPER
    if self.opponent == self.PAPER:
      return self.SCISSOR
    if self.opponent == self.SCISSOR:
      return self.ROCK
  
  def draw(self) -> str:
    return self.opponent

  def lose(self) -> str:
    if self.opponent == self.ROCK:
      return self.SCISSOR
    if self.opponent == self.PAPER:
      return self.ROCK
    if self.opponent == self.SCISSOR:
      return self.PAPER

  def my_move(self) -> str:
    if self.my == self.WIN:
      return self.win()
    if self.my == self.DRAW:
      return self.draw()
    return self.lose()

  def score_value(self, move) -> int:
    if move == 'A':
      return 1
    if move == 'B':
      return 2
    if move == 'C':
      return 3

  def score(self) -> int:
    score = self.score_value(self.my_move())
    
    if (self.my == self.WIN):
      score += 6
    elif (self.my == self.DRAW):
      score += 3

    return score

def test_move():
  m = Move('A Y')
  assert m.opponent == 'A'
  assert m.my == 'Y'
  assert m.win() == 'B'
  assert m.lose() == 'C'
  assert m.draw() == 'A'
  assert m.score() == 4

  m = Move('B X')
  assert m.score() == 1

  m = Move('C Z')
  assert m.score() == 7

if __name__ == '__main__':
  moves = [Move(m) for m in input.as_list()]
  print(sum(map(lambda m: m.score(), moves)))
