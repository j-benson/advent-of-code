#!/usr/bin/env python3

import argparse, os

def create_file(file, contents):
  if not os.path.exists(file):
    with open(file, 'w') as out:
      out.write(contents)

if __name__ == "__main__":
  argp = argparse.ArgumentParser()
  argp.add_argument('day')
  args = argp.parse_args()

  module_base = f'advent_{args.day.zfill(2)}'
  module_solvers = [
    f'{module_base}_1',
    f'{module_base}_2',
  ]
  file_base = 'solvers/'
  file_solvers = [ f'{file_base}{module}.py' for module in module_solvers ]
  file_test = f'{file_base}{module_base}_test.py'

  for f in file_solvers:
    create_file(
      f,
'''
def solve(input):
  pass

'''
    )

  create_file(
    file_test,
f'''import {", ".join(module_solvers)}

input = [
  
]

def test_1():
  pass

def test_2():
  pass

'''
  )
