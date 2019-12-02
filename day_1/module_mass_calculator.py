#!/usr/bin/python3

import argparse

from pathlib import Path
from typing import List, Iterator

def _main():
   parser = argparse.ArgumentParser()
   parser.add_argument('module_file')
   parser.add_argument('--fuel-cost', action='store_true')
   args = parser.parse_args()

   print(args)
   modules = list( _parse_ints(args.module_file))
   #print(modules)
   module_total = 0
   for rocket_module in modules:
      module_cost = rocket_module // 3 - 2
      #print(module_cost)
      if args.fuel_cost:
         module_cost += _calculate_fuel(module_cost)
      #print(module_cost)
      module_total += module_cost

   print(module_total)

def _parse_ints(input_file: str) -> Iterator[int]:
   with open(input_file, 'r') as i_file:
      for line in i_file:
         yield int(line)

def _calculate_fuel(fuel_amount: int) -> int:
   required_fuel = fuel_amount // 3 - 2
   if required_fuel > 0:
      return required_fuel + _calculate_fuel(required_fuel)

   if required_fuel < 0:
      required_fuel = 0

   return required_fuel

if __name__ == "__main__":
   _main()
