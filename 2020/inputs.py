import requests, os

def get_input(day):
  filename = f'inputs/advent_{str(day).zfill(2)}.txt'
  
  if not os.path.exists(filename):
    res = requests.get(f'https://adventofcode.com/2020/day/{str(day)}/input')
    if res.status_code != 200:
      raise Exception(f'Cannot get day {day} input. Reason: {res.text}')
    with open(filename, 'w') as data:
      data.write(res.text)

  with open(filename) as data:
    return [ line.rstrip('\n') for line in data.readlines() ]
