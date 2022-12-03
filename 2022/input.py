#!/usr/bin/env python3

import argparse, os, requests, sys
import session

YEAR = '2022'

def as_list(lines = None):
  if lines is None:
    lines = sys.stdin.readlines()
  return [ line.rstrip('\n') for line in lines ]

def get_input(day, year = YEAR):
  os.makedirs('inputs', exist_ok=True)
  filename = f'inputs/{day.zfill(2)}.txt'
  
  if not os.path.exists(filename):
    res = requests.get(
      f'https://adventofcode.com/{year}/day/{day}/input',
      headers={
        'cookie': f'session={session.login()};'
      }
    )
    if res.status_code == 400:
      session.logout()
    if res.status_code != 200:
      raise Exception(f'Cannot get day {day} input. Reason: {res.text}')
    with open(filename, 'w') as data:
      data.write(res.text)

  with open(filename) as data:
    return data.readlines()

if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  group = ap.add_mutually_exclusive_group(required=True)
  group.add_argument('-d', '--day')
  ap.add_argument('-y', '--year', default=YEAR)
  group.add_argument('-f', '--file')
  args = ap.parse_args()

  if args.file is not None:
    with open(args.file) as data:
      lines = data.readlines()
  else:
    lines = get_input(args.day, args.year)
  
  for line in lines:
    print(line, end='')
