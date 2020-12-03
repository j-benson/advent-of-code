import re

claim_re = re.compile(r'#([0-9]+)\s@\s([0-9]+),([0-9]+):\s([0-9]+)x([0-9]+)')

class Claim(object):
  def __init__(self, claim):
    match = claim_re.search(claim)
    if not match:
      raise Exception('Invalid claim: {}'.format(claim))

    self.id = match.group(1)
    self.x = int(match.group(2))
    self.y = int(match.group(3))
    self.width = int(match.group(4))
    self.height = int(match.group(5))
    
def __str__(self):
  return '#{} ({},{}) {}x{}'.format(self.id, self.x, self.y, self.width, self.height)