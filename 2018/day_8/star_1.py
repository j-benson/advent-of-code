with open("data.txt") as data:
  line = data.readline()

numbers = line.split(" ")

HEADER_LEN = 2
nodes = dict()

def traverse(i):
  child_nodes, meta_len = int(numbers[i]), int(numbers[i+1])
  if child_nodes == 0:
    length = HEADER_LEN + meta_len
    meta_index = i + HEADER_LEN
    node = (i, length, meta_index, meta_len)
    nodes[i] = node
    return node
  else:
    child_nodes_length = 0
    for c in range(0, child_nodes):
      child_node = traverse(i + HEADER_LEN + child_nodes_length)
      child_nodes_length += child_node[1]
    length = HEADER_LEN + meta_len + child_nodes_length
    meta_index = i + HEADER_LEN + child_nodes_length
    node = (i, length, meta_index, meta_len)
    nodes[i] = node
    return node

traverse(0)

meta = [ int(numbers[i]) for n in nodes.keys() for i in range(nodes[n][2], nodes[n][2] + nodes[n][3]) ]

print(sum(meta))
