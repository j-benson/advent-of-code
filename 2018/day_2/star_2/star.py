with open('data.txt') as data:
  ids = data.readlines()

def find_similar():
  for id in ids:
    for other_id in ids:
      differences = []
      for i in range(0, len(id) -1):
        if id[i] != other_id[i]:
          differences.append(i)
      if len(differences) == 1:
        return (id, other_id, differences)

id_1, id_2, diff = find_similar()

print(id_1)
print(id_2)
print(diff)