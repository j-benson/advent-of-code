import sys

lines = list(map(lambda line : line.rstrip('\n'), sys.stdin.readlines()))

elf_calory_pairs = []

elf_id = 1
calory_count = 0
for line in lines:
  if line != '':
    calory_count += int(line)
  else:
    elf_calory_pairs.append((calory_count, elf_id))
    elf_id += 1
    calory_count = 0
if calory_count > 0:
  elf_calory_pairs.append((calory_count, elf_id))

sorted_elf_calory_pairs = sorted(elf_calory_pairs, reverse=True)
total = 0
for i in range(3):
  elf_calories = sorted_elf_calory_pairs[i]
  total += elf_calories[0]
  print(elf_calories)
print(f'total: {total}')
