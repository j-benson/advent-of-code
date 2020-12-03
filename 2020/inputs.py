import requests, os, json

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
