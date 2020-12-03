from collections import defaultdict

nodes = set()
edges = defaultdict(set)
with open('../data.txt') as data:
  for line in data.readlines():
    nodes.add(line[5])
    nodes.add(line[36])
    edges[line[36]].add(line[5])

node_order = []
ordered_nodes = set()
available = nodes.difference(edges.keys())

def pick_next():
  next_node = sorted(available)[0]
  available.remove(next_node)

  node_order.append(next_node)
  ordered_nodes.add(next_node)


pick_next()
while len(nodes) != len(ordered_nodes):
  for node in nodes:
    if node not in ordered_nodes and len(edges[node] - ordered_nodes) == 0:
      available.add(node)
  pick_next()

print("".join(node_order))
