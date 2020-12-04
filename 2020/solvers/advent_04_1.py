import re

def solve(input):
  passports = create_passports(input)
  valid = 0
  for passport in passports:
    if passport.valid(): valid += 1
  return valid

def create_passports(input):
  passports = []
  passport_lines = []
  for line in input:
    if line == '':
      passports.append(Passport(passport_lines))
      passport_lines = []
    else:
      passport_lines.append(line)
  if len(passport_lines) > 0:
    passports.append(Passport(passport_lines))
  return passports


class Passport:
  def __init__(self, lines):
    self.props = dict()
    pattern = re.compile(r'([a-z]+:[a-z0-9#]+)+', flags=re.IGNORECASE)
    for line in lines:
      match = pattern.findall(line)
      if match != None:
        for m in match:
          n = m.split(':')
          self.props[n[0]] = n[1]

  def valid(self):
    required_props = {
      'byr',
      'iyr',
      'eyr',
      'hgt',
      'hcl',
      'ecl',
      'pid',
    }
    optional_props = {
      'cid'
    }
    return len(required_props.difference(set(self.props)).difference(optional_props)) == 0
