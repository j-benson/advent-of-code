with open("data.txt") as data:
  line = data.readline()

numbers = line.split(" ")
numbers = [int(n) for n in numbers]

HEADER_LEN = 2
nodes = dict()

class Node():
  def __init__(self, i, length=None, meta_index=None, meta_len=None):
    self.i = i
    self.length = length
    self.meta_index = meta_index
    self.meta_len = meta_len
    self.children = []
    self.value = None
  def meta_indexes(self):
    return range(self.meta_index, self.meta_index + self.meta_len)
  def has_child(self, i):
    return i > 0 and i <= len(self.children)
  def get_child_node(self, i):
    return nodes[self.children[i - 1]]

def traverse(i):
  child_nodes, meta_len = numbers[i], numbers[i+1]
  if child_nodes == 0:
    node = Node(i=i, length=HEADER_LEN + meta_len, meta_index=i + HEADER_LEN, meta_len=meta_len)
    node.value = sum([ numbers[i] for i in node.meta_indexes() ])
    nodes[i] = node
    return node
    
  else:
    node = Node(i)
    child_nodes_length = 0
    for c in range(0, child_nodes):
      child_node = traverse(i + HEADER_LEN + child_nodes_length)
      node.children.append(child_node.i)
      child_nodes_length += child_node.length

    node.length = HEADER_LEN + meta_len + child_nodes_length
    node.meta_index = i + HEADER_LEN + child_nodes_length
    node.meta_len = meta_len

    node.value = 0
    for meta_index in node.meta_indexes():
      if node.has_child(numbers[meta_index]):
        child = node.get_child_node(numbers[meta_index])
        node.value += child.value
    
    nodes[i] = node
    return node

traverse(0)

meta = [ numbers[i] for n in nodes.keys() for i in nodes[n].meta_indexes() ]

print(sum(meta))
print(nodes[0].value)
