with open('data.txt') as data:
  freq_set = set()
  freq = 0
  answer = -1
  lines = data.readlines()
  loops = 0
  while answer == -1:
    loops += 1
    for v in lines:
      print(v[:-1], end=" | ")
      freq += int(v) 
      print(freq)
      if freq in freq_set:
        answer = freq
        break
      freq_set.add(freq)

print(answer)
print(loops)