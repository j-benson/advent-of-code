#!/usr/bin/env python3

import argparse, importlib, inputs
from datetime import datetime

def import_solver(day, part):
  try:
    return importlib.import_module(f'solvers.advent_{day.zfill(2)}_{part}')
  except ImportError as e:
    raise Exception(f'Cannot find solver for day {day} part {part}. Reason: {str(e)}')

def print_table(lines):
  width = max(map(lambda line: len(line), lines))
  separator = ''.ljust(width, '-') + '\n'
  print(separator.join([ line + '\n' for line in lines ]), end='')

if __name__ == "__main__":
  argp = argparse.ArgumentParser()
  argp.add_argument('day')
  argp.add_argument('--part', '-p', default='1')
  argp.add_argument('--submit', '-s', action='store_true')
  args = argp.parse_args()
  
  try:
    solver = import_solver(args.day, args.part)
    input = inputs.get_input(args.day)
    time_start = datetime.now()
    output = solver.solve(input)
    time_end = datetime.now()
    print_table([
      str(output),
      f'solved in {str(time_end - time_start)}'
    ])
    if args.submit:
      inputs.submit_answer(args.day, args.part, output)
      print('⭐️')
  except Exception as e:
    print(f'{type(e).__name__}: {str(e)}')
