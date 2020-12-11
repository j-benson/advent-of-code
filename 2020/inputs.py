import requests, os, json, re

config_filename = '.adventofcode'

def load_config():
  try:
    with open(config_filename, 'r') as file:
      return json.load(file)
  except:
    return {}

def update_config(config):
  with open(config_filename, 'w') as file:
    json.dump(config, file)

def login():
  config = load_config()
  if 'session' not in config:
    print('Paste AoC session cookie value:')
    config['session'] = input('> ')
    update_config(config)
  return config['session']

def logout():
  config = load_config()
  config.pop('session', None)
  update_config(config)

def get_input(day):
  filename = f'inputs/advent_{str(day).zfill(2)}.txt'
  
  if not os.path.exists(filename):
    session = login()
    res = requests.get(
      f'https://adventofcode.com/2020/day/{str(day)}/input',
      headers={
        'cookie': f'session={session};'
      }
    )
    if res.status_code == 400:
      logout()
    if res.status_code != 200:
      raise Exception(f'Cannot get day {day} input. Reason: {res.text}')
    with open(filename, 'w') as data:
      data.write(res.text)

  with open(filename) as data:
    return [ line.rstrip('\n') for line in data.readlines() ]

def split_input(input, separator=''):
  out = []
  group = []
  for line in input:
    if line == separator:
      out.append(group)
      group = []
    else:
      group.append(line)
  if len(group) > 0:
    out.append(group)
  return out


def submit_answer(day, part, answer):
  session = login()
  payload = { 'level': str(part), 'answer': str(answer) }
  res = requests.post(
    f'https://adventofcode.com/2020/day/{day}/answer',
    headers={
      'cookie': f'session={session};'
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
    raise Exception('Answer not submitted.')
