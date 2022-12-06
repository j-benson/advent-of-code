#!/usr/bin/env python3

import input

def find_marker(marker_length: int, data: str):
  last_chars = []
  for i in range(len(data)):
    c = data[i]
    last_chars.append(c)
    if (len(last_chars) > marker_length):
      last_chars.pop(0)
    if len(set(last_chars)) == marker_length:
      return i + 1

if __name__ == '__main__':
  data = input.as_list()[0]
  print(find_marker(4, data))
  print(find_marker(14, data))
