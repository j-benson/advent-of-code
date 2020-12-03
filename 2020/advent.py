#!/usr/bin/env python3

import argparse, importlib, inputs

def import_solver(day, part):
  try:
    return importlib.import_module(f'advent_{day.zfill(2)}_{part}')
  except ImportError:
    raise Exception(f'Cannot find solver for day {day} part {part}')

if __name__ == "__main__":
  argp = argparse.ArgumentParser()
  argp.add_argument('day')
  argp.add_argument('--part', '-p', default='1')
  args = argp.parse_args()
  
  try:
    solver = import_solver(args.day, args.part)
    output = solver.solve(inputs.get_input(args.day))
    print(output)
  except Exception as e:
    print(str(e))
