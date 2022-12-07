from day7 import TerminalReader

def test_terminal_reader_directories():
  reader = TerminalReader()
  
  reader.readline('$ cd /')
  assert '/' == reader.pwd()

  reader.readline('$ cd a')
  assert '/a' == reader.pwd()

  reader.readline('$ cd b')
  assert '/a/b' == reader.pwd()

  reader.readline('$ cd ..')
  assert '/a' == reader.pwd()
