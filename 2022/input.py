#!/usr/bin/env python3

import argparse, os, requests
import session

YEAR = '2022'

def to_list(lines):
  return [ line.rstrip('\n') for line in lines ]

def get_input_lines(day, year = YEAR):
  raw_input = get_input_raw(day, year)
  return to_list(raw_input)

def get_input_raw(day, year = YEAR):
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
  ap.add_argument('-d', '--day', required=True)
  ap.add_argument('-y', '--year', default=YEAR)
  args = ap.parse_args()
  lines = get_input_raw(args.day, args.year)
  for line in lines:
    print(line, end='')
