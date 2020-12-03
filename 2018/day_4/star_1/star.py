from datetime import datetime, timedelta

def parse_line(line):
  date = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
  message = line[19:]
  return (date, message)

with open('data.txt') as data:
  unordered_list = [parse_line(line) for line in data.readlines()]

ordered_list = sorted(unordered_list, key= lambda i : i[0])

guard_log = dict() # guard_id -> ( fell_asleep, woke_up, time_asleep )

guard = None
fell_asleep = None

## Parse the ordered guard sleep log
for log_entry in ordered_list:
  timestamp = log_entry[0]
  message = log_entry[1]
  
  if message.startswith("Guard"):
    guard = message[7:message.index(" ", 7)]
  elif message.startswith("falls asleep"):
    fell_asleep = timestamp
  elif message.startswith("wakes up"):
    if fell_asleep == None:
      raise Exception("WTF")
    time_asleep = timestamp - fell_asleep
    sleep_entry = (fell_asleep, timestamp, time_asleep)
    if guard in guard_log:
      guard_log[guard].append(sleep_entry)
    else:
      guard_log[guard] = [ sleep_entry ]
    fell_asleep = None

## Create a tuple for sorting to find the guard that sleeps the most
total_sleep_time = []
for g_id in guard_log.keys():
  total_time = sum([log_entry[2] for log_entry in guard_log[g_id]], timedelta())
  total_sleep_time.append((g_id, total_time))
total_sleep_time.sort(reverse=True, key=lambda elem : elem[1])

sleepy_guard_id = total_sleep_time[0][0]
print(sleepy_guard_id)


## Find the sleepy guards most slept minute
sleep_log = guard_log[sleepy_guard_id]
sleep_minute_count = dict()
for i in range(0, 60):
  sleep_minute_count[i] = 0

for log_entry in sleep_log: # ( fell_asleep, woke_up, time_asleep )
  fell_asleep = log_entry[0]
  time_asleep = log_entry[2]

  start_sleep_minute = int(fell_asleep.minute)
  end_sleep_minute = start_sleep_minute + int(time_asleep.total_seconds() / 60)
  for minute in range(start_sleep_minute, end_sleep_minute):
    sleep_minute_count[minute] += 1

sleep_minute_count = [(k, sleep_minute_count[k]) for k in sleep_minute_count.keys()]
sleep_minute_count.sort(reverse=True, key=lambda elem : elem[1])

sleepy_minute = sleep_minute_count[0][0]
print(sleepy_minute)

checksum = int(sleepy_guard_id) * sleepy_minute
print(checksum)