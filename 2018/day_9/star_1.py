class Game():
  def __init__(self, player_count, last_marble):
    self.players = [Player(self) for n in range(0, player_count)]
    self.marble_pile = [Marble(n) for n in range(last_marble, -1, -1)]
    
    self.circle = Circle(self.pick_up_marble())

  def play(self):
    while self.marble_pile:
      ## round start
      for player in self.players:
        if not self.marble_pile:
          break
        self.current_player = player
        self.current_player.take_turn()
      ## round end

  def pick_up_marble(self):
    return self.marble_pile.pop()

  def add_marble_to_cirle(self, marble):
    self.circle.add_marble(marble)
  
  def remove_marble_from_circle(self):
    return self.circle.remove_marble()
    
class Circle():
  def __init__(self, first_marble):
    self.marbles = [ first_marble ]
    self.current_marble = 0

  def add_marble(self, marble):
    next_index = self.current_marble + 2
    if next_index > len(self.marbles):
      next_index -= len(self.marbles)
    self.marbles.insert(next_index, marble)
    self.current_marble = next_index

  def remove_marble(self):
    index = self.current_marble - 7
    if index < 0:
      index += len(self.marbles)
    removed = self.marbles.pop(index)
    self.current_marble = index
    return removed


class Marble():
  def __init__(self, number):
    self.number = number

class Player():
  def __init__(self, game):
    self.game = game
    self.score = 0
    self.marbles = []

  def take_turn(self):
    marble = self.game.pick_up_marble()
    if marble.number % 23 == 0:
      self.keep_marble(marble)
      self.keep_marble(self.game.remove_marble_from_circle())
    else:
      self.game.add_marble_to_cirle(marble)
  
  def keep_marble(self, marble):
    self.marbles.append(marble)
    self.score += marble.number


game = Game(441, 71032)
game.play()

player_scores = sorted(game.players, key=lambda p:p.score, reverse=True)
print(player_scores[0].score)
