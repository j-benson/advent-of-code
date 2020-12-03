from claim import Claim

with open('data.txt') as data:
  claims = [Claim(line) for line in data.readlines()]

fabric = dict()
fabric_size = 1000
for x in range(0, fabric_size):
  for y in range(0, fabric_size):
    fabric[(x, y)] = None

for claim in claims:
  for x in range(claim.x, claim.x + claim.width):
    for y in range(claim.y, claim.y + claim.height):
      if fabric[(x, y)] == None:
        fabric[(x, y)] = [claim.id]
      else:
        fabric[(x, y)].append(claim.id)

isolated_claims = []
for claim in claims:
  is_isolated = True
  for x in range(claim.x, claim.x + claim.width):
    for y in range(claim.y, claim.y + claim.height):
      if len(fabric[(x, y)]) != 1:
        is_isolated = False
        break
    if not is_isolated:
      break
  if is_isolated:
    isolated_claims.append(claim.id)

print(isolated_claims)
