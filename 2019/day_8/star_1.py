from collections import defaultdict

with open('input') as data:
  image = data.readline()
width = 25
height = 6

digits = [ int(d) for d in list(image) ] 

# Split raw digits into rows
rows = []
for row_start in range(0, len(digits), width):
  rows.append(digits[row_start: row_start + width])

# Split rows into layers
layer_count = int(len(rows) / height)
layers = []
for layer_start in range(0, len(rows), height):
  layers.append(rows[layer_start:layer_start+height])

if __name__ == "__main__":
  # Count digit occurances
  digit_count = { layer : defaultdict(int) for layer in range(layer_count) }
  for layer_i in range(len(layers)):
    for row in layers[layer_i]:
      for digit in row:
        digit_count[layer_i][digit] += 1 
  
  # Find layer with least zeros
  zeros = []
  for layer_i in range(len(layers)):
    zeros.append((digit_count[layer_i][0], layer_i))
  zeros.sort()
  layer = zeros[0][1]

  # Count digit occurances
  digit_count = { layer : defaultdict(int) for layer in range(layer_count) }
  for layer_i in range(len(layers)):
    for row in layers[layer_i]:
      for digit in row:
        digit_count[layer_i][digit] += 1 
  
  # Checksum
  print(f'layer: {layer}')
  print(digit_count[layer][1] * digit_count[layer][2])
