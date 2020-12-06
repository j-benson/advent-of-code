from inputs import split_input

def solve(input):
  groups = [ Group(data) for data in split_input(input) ]
  return sum(map(lambda group: len(group.questions), groups))

class Group:
  def __init__(self, data):
    self.questions = set()
    for person in data:
      for question in person:
        self.questions.add(question)
