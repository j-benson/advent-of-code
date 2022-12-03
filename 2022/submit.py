#!/usr/bin/env python3

import argparse, input, sys, requests, re, session

def submit_answer(year, day, part, answer):
  payload = { 'level': str(part), 'answer': str(answer) }
  res = requests.post(
    f'https://adventofcode.com/{year}/day/{day}/answer',
    headers={
      'cookie': f'session={session.login()};'
    },
    data=payload
  )
  if res.status_code == 200:
    if re.search(r'That\'s not the right answer', res.text):
      raise Exception('That\'s not the right answer.')
    elif re.search('You gave an answer too recently', res.text):
      msg = 'You gave an answer too recently.'
      match = re.match(r'You have [0-9a-z ]* left to wait.?', res.text)
      if match: msg += ' ' + match.group(0)
      raise Exception(msg)
  else:
    raise Exception(f'Answer not submitted ({res.status_code}).')

if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  ap.add_argument('-d', '--day', required=True)
  ap.add_argument('-p', '--part', required=True)
  ap.add_argument('-y', '--year', default=input.YEAR)
  args = ap.parse_args()

  answer = sys.stdin.readlines().pop().rstrip('\n')
  try:
    submit_answer(args.year, args.day, args.part, answer)
    print('⭐️')
  except Exception as e:
    print(e)
