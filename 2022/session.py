#!/usr/bin/env python3

import json

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
