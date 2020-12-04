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
    return self._valid_props() and self._valid_data()

  def _valid_props(self):
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

  def _valid_data(self):
    return self._valid_byr(self.props['byr']) \
      and self._valid_iyr(self.props['iyr']) \
      and self._valid_eyr(self.props['eyr']) \
      and self._valid_hgt(self.props['hgt']) \
      and self._valid_hcl(self.props['hcl']) \
      and self._valid_ecl(self.props['ecl']) \
      and self._valid_pid(self.props['pid'])

  def _valid_byr(self, value):
    return self._valid_year(value, 1920, 2002)
  
  def _valid_year(self, value, min, max):
    return len(value) == 4 and int(value) >= min and int(value) <= max

  def _valid_iyr(self, value):
    return self._valid_year(value, 2010, 2020)
  
  def _valid_eyr(self, value):
    return self._valid_year(value, 2010, 2030)

  def _valid_hgt(self, value):
    if 'in' in value:
      return self._valid_hgt_in(value)
    elif 'cm' in value:
      return self._valid_hgt_cm(value)
    else:
      return False

  def _valid_hgt_in(self, value):
    int_value = int(value.rstrip('in'))
    return int_value >= 59 and int_value <= 76

  def _valid_hgt_cm(self, value):
    int_value = int(value.rstrip('cm'))
    return int_value >= 150 and int_value <= 193

  def _valid_hcl(self, value):
    return re.match(r'^#[0-9a-f]{6}$', value, flags=re.IGNORECASE) != None

  def _valid_ecl(self, value):
    valid = {
      'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    }
    return value in valid

  def _valid_pid(self, value):
    return re.match(r'^[0-9]{9}$', value, flags=re.IGNORECASE)
