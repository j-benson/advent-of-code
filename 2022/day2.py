#!/usr/bin/env python3

import sys, input

class Move:
  def __init__(self, value) -> None:
    self.ROCK = [ 'A', 'X' ]
    self.PAPER = [ 'B', 'Y' ]
    self.SCISSOR = [ 'C', 'Z' ]
    self.opponent, self.my = value.split(' ')

  def is_draw(self) -> bool:
    return (self.my in self.ROCK and self.opponent in self.ROCK) \
      or (self.my in self.PAPER and self.opponent in self.PAPER) \
      or (self.my in self.SCISSOR and self.opponent in self.SCISSOR)
  
  def is_win(self) -> bool:
    return (self.my in self.ROCK and self.opponent in self.SCISSOR) \
      or (self.my in self.PAPER and self.opponent in self.ROCK) \
      or (self.my in self.SCISSOR and self.opponent in self.PAPER)

  def score(self) -> int:
    score = 0
    if self.my in self.ROCK:
      score += 1
    elif self.my in self.PAPER:
      score += 2
    elif self.my in self.SCISSOR:
      score += 3
    
    if (self.is_win()):
      score += 6
    elif (self.is_draw()):
      score += 3

    return score

def test_move():
  m = Move('A Y')
  assert m.opponent == 'A'
  assert m.my == 'Y'
  assert m.is_win() == True
  assert m.is_draw() == False
  assert m.score() == 8

  m = Move('B X')
  assert m.is_win() == False
  assert m.is_draw() == False
  assert m.score() == 1

  m = Move('C Z')
  assert m.is_win() == False
  assert m.is_draw() == True
  assert m.score() == 6

class Strategy:
  def __init__(self, value) -> None:
    self.moves = [ Move(m) for m in value ]

if __name__ == '__main__':
  moves = [Move(m) for m in input.to_list(sys.stdin.readlines())]
  print(sum(map(lambda m: m.score(), moves)))
