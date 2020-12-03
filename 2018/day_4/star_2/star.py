from collections import defaultdict
from datetime import datetime, timedelta

def parse_line(line):
  date = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
  message = line[19:]
  return (date, message)

class Guard():
  guards = dict()

  def __init__(self, id):
    self.id = id
    self.guards[id] = self
    self.sleep_record = SleepRecord()

  def asleep_at(self, time):
    self.sleep_record.asleep_at(time)

  def awake_at(self, time):
    self.sleep_record.awake_at(time)

class SleepRecord():
  def __init__(self):
    self.sleeps = []
    self.total_minutes_asleep = 0
    self.minutes_asleep = defaultdict(int)

  def asleep_at(self, time):
    self.sleeps.append(Sleep(time))

  def awake_at(self, time):
    self.sleeps[-1].awake(time)

    self.total_minutes_asleep += self.sleeps[-1].total_minutes_asleep()
    for m in self.sleeps[-1].minutes_asleep():
      self.minutes_asleep[m] += 1

  def top_minutes(self):
    return sorted([(m, self.minutes_asleep[m]) for m in self.minutes_asleep], key=lambda i:i[1], reverse=True)


class Sleep():
  def __init__(self, time_asleep):
    self.time_asleep = time_asleep
  
  def awake(self, time_awake):
    self.time_awake = time_awake

  def total_minutes_asleep(self):
    return int((self.time_awake - self.time_asleep).total_seconds() / 60)
  
  def minutes_asleep(self):
    return [m for m in range(self.time_asleep.minute, self.time_awake.minute)]

def highest_sleep_time():
  total_sleep_time = [(Guard.guards[g].id, Guard.guards[g].sleep_record.total_minutes_asleep) for g in Guard.guards]
  guard_id, sleep_time = sorted(total_sleep_time, key=lambda i:i[1], reverse=True)[0]
  top_minute = Guard.guards[guard_id].sleep_record.top_minutes()[0][0]
  return int(guard_id) * top_minute

def most_freqent_minute():
  gs = [Guard.guards[g] for g in Guard.guards]
  gs = list(filter(lambda g: len(g.sleep_record.minutes_asleep) > 0, gs))
  m = sorted([ (g.id, g.sleep_record.top_minutes()[0]) for g in gs ], key=lambda i:i[1][1], reverse=True)[0]
  return int(m[0]) * m[1][0]

if __name__ == "__main__":
  with open('data.txt') as data:
    unordered_list = [parse_line(line) for line in data.readlines()]
  ordered_list = sorted(unordered_list, key= lambda i : i[0])

  guard = None
  ## Parse the ordered guard sleep log
  for log_entry in ordered_list:
    timestamp = log_entry[0]
    message = log_entry[1]
    
    if message.startswith("Guard"):
      g = message[7:].split(" ")[0]
      if g not in Guard.guards:
        Guard.guards[g] = Guard(g)
      guard = Guard.guards[g]
    elif message.startswith("falls asleep"):
      guard.asleep_at(timestamp)
    elif message.startswith("wakes up"):
      guard.awake_at(timestamp)

print(most_freqent_minute())