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
available_nodes = nodes.difference(edges.keys())
pending_nodes = set()
time = 0
workers = [None for i in range(0, 5)] # [ (node, finishes), .. ] 

def pick_next():
  if len(available_nodes) == 0:
    return None
  return sorted(available_nodes)[0]

def free_worker():
  for i in range(0, len(workers)):
    if workers[i] == None:
      return i
  return None

def check_for_completed():
  for i, worker in enumerate(workers):
    if worker == None:
      continue
    node, complete_time = worker
    if complete_time == time:
      complete_node(node)
      workers[i] = None

def complete_node(node):
  pending_nodes.remove(node)
  ordered_nodes.add(node)
  node_order.append(node)

def start_available():
  while pick_next() is not None and free_worker() is not None:
    start_node(pick_next(), free_worker())

def start_node(node, worker):
  complete_time = time + ord(node) - 64 + 60
  workers[worker] = (node, complete_time)
  available_nodes.remove(node)
  pending_nodes.add(node)

def check_for_available():
  for node in nodes:
    if node not in pending_nodes and node not in ordered_nodes and len(edges[node] - ordered_nodes) == 0:
      available_nodes.add(node)



while len(nodes) != len(ordered_nodes):
  check_for_completed()
  check_for_available()
  start_available()

  time += 1

print("".join(node_order))
print(time - 1)
