with open('data.txt') as data:
  twos = 0
  threes = 0
  
  for id in data.readlines():
    char_to_count = dict()
    for i in range(0, len(id)):
      if id[i] in char_to_count:
        char_to_count[id[i]] += 1
      else:
        char_to_count[id[i]] = 1
    
    count_to_char = dict()
    for c in char_to_count:
      if char_to_count[c] in count_to_char:
        count_to_char[char_to_count[c]] += 1
      else:
        count_to_char[char_to_count[c]] = 1

    if 2 in count_to_char: 
      twos += 1
    if 3 in count_to_char: 
      threes += 1
  
  checksum = twos * threes
  print('{} * {} = {}'.format(twos, threes, checksum))

