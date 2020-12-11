from solvers.advent_08_1 import GameBoy
from copy import deepcopy

def solve(input):
  jmp_nops = jmp_nop_positions(input)
  while (True):
    assert len(jmp_nops) > 0
    instructions = swap_opcode(input, jmp_nops.pop())
    try:
      return execute(instructions)
    except Exception:
      continue

def jmp_nop_positions(instructions):
  jmp_nops = []
  for i in range(0, len(instructions)):
    if 'jmp' in instructions[i] or 'nop' in instructions[i]:
      jmp_nops.append(i)
  return jmp_nops

def swap_opcode(instructions, i):
  copy = list(instructions)
  if 'jmp' in copy[i]:
    copy[i] = copy[i].replace('jmp', 'nop')
  elif 'nop' in copy[i]:
    copy[i] = copy[i].replace('nop', 'jmp')
  return copy

def execute(bootcode):
  gameboy = GameBoy(bootcode)
  previous_program_counters = set()

  while (True):
    if gameboy.program_counter in previous_program_counters:
      raise Exception('Program looped')
    if gameboy.program_counter < 0 or gameboy.program_counter >= len(bootcode):
      break
    previous_program_counters.add(gameboy.program_counter)
    gameboy.next_instruction()
  return gameboy.accumulator
