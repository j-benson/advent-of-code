#!/usr/bin/env python3

import input, re

class TerminalReader:
  _cd_pattern = re.compile('^\\$ (cd) ([\\w./]+)$')
  _ls_pattern = re.compile('^\\$ (ls)$')
  _dir_pattern = re.compile('^(dir) [\\w]+$')
  _file_pattern = re.compile('^([\\d]+) ([\\w.]+)$')
  def __init__(self) -> None:
    self.dir_stack = []
    self.command = ''

  def pwd(self):
    return '/' + '/'.join(self.dir_stack)

  def readline(self, line):
    commands = [
      self._cd_pattern,
      self._ls_pattern
    ]
    outputs = [
      self._dir_pattern,
      self._file_pattern
    ]
    for c in commands:
      match = c.search(line)
      if match:
        self._handle_command(match)
        return
    for o in outputs:
      match = o.search(line)
      if match:
        self._handle_output(match)
        return
    raise Exception(f'unknown line: {line}')

  def _handle_command(self, match):
    self.command = match.group(1)
    if (self.command == 'cd'):
      dir = match.group(2)
      if dir == '/':
        self.dir_stack = []
      elif dir == '..':
        self.dir_stack.pop()
      else:
        self.dir_stack.append(dir)

  def _handle_output(self, match):
    if self.command != 'ls':
      raise Exception(f'unknown command: {self.command}')
    if match.group(1) == 'dir':
      return

class FileSystem:
  pass

if __name__ == '__main__':
  lines = input.as_list()
