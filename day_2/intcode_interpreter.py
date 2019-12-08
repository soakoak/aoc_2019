#!/usr/bin/python

import argparse

from pathlib import Path
from typing import List, Iterator

def _main():
   parser = argparse.ArgumentParser()
   parser.add_argument('opcode_file')
   args = parser.parse_args()

   print(args)
   values = list(_parse_ints(args.opcode_file))

   # values before crash
   values[1] = 12
   values[2] = 2

   opcode_pos = 0
   chunk_no = 0
   while True:
      opcode_pos = chunk_no * 4
      opcode = values[opcode_pos]
      value_1_pos = values[opcode_pos + 1]
      value_1 = values[value_1_pos]
      value_2_pos = values[opcode_pos + 2]
      value_2 = values[value_2_pos]
      edited_position = values[opcode_pos + 3]

      if opcode is 1:
         print(f'[{edited_position}] = {value_1} + {value_2}')
         values[edited_position] = value_1 + value_2
      elif opcode is 2:
         print(f'[{edited_position}] = {value_1} * {value_2}')
         values[edited_position] = value_1 * value_2
      elif opcode is 99:
         break

      chunk_no += 1

   print(values[0])
   '''
   for chunk in _list_to_chunks(values, 4):

      edited_position = chunk_no + chunk[3]
      if chunk[0] is 1:
         values[edited_position] = 
   '''
   
def _parse_ints(input_file: str) -> List[int]:
   with open(input_file, 'r') as i_file:
      return [ int(n) for n in i_file.read().split(',') ]    

def _list_to_chunks(lst, n):
   for i in range(0, len(lst), n):
      yield lst[i:i + n]

if __name__ == "__main__":
   _main()
