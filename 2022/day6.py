#!/usr/bin/env python3

import input

if __name__ == '__main__':
  data = input.as_list()[0]
  last_chars = []
  for i in range(len(data)):
    c = data[i]
    last_chars.append(c)
    if (len(last_chars) > 4):
      last_chars.pop(0)
    if len(set(last_chars)) == 4:
      print(i + 1)
      exit()
    
