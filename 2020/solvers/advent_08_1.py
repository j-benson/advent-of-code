def solve(input):
  gameboy = GameBoy(input)
  previous_program_counters = set()
  last_accumalator_value = gameboy.accumulator

  while (True):
    if gameboy.program_counter in previous_program_counters:
      return last_accumalator_value

    previous_program_counters.add(gameboy.program_counter)
    
    gameboy.next_instruction()

    if gameboy.program_counter in previous_program_counters:
      return last_accumalator_value
    
    last_accumalator_value = gameboy.accumulator


class GameBoy:
  def __init__(self, bootcode):
    self.bootcode = [ instruction.split(' ') for instruction in bootcode ]
    self.program_counter = 0
    self.accumulator = 0
    self.opcodes = {
      'nop': self._nop,
      'acc': self._acc,
      'jmp': self._jmp,
    }

  def next_instruction(self):
    opcode = self.bootcode[self.program_counter][0]
    data = self.bootcode[self.program_counter][1]
    self.opcodes[opcode](data)

  def _nop(self, data):
    self.program_counter += 1

  def _acc(self, data):
    self.accumulator += int(data)
    self.program_counter += 1

  def _jmp(self, data):
    self.program_counter += int(data)

  def __repr__(self):
    return f'GameBoy(program_counter={self.program_counter}, accumulator={self.accumulator})'
