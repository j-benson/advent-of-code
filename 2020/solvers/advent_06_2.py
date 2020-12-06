from inputs import split_input
from collections import defaultdict

def solve(input):
  groups = [ Group(data) for data in split_input(input) ]
  return sum(map(lambda group: group.all_answered(), groups))

class Group:
  def __init__(self, data):
    self.questions = defaultdict(int)
    self.people = len(data)
    for person in data:
      for question in person:
        self.questions[question] += 1

  def all_answered(self):
    return len(list(filter(lambda question: self.questions[question] == self.people, self.questions)))
