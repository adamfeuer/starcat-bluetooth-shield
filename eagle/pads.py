#!/usr/bin/env python

import sys, collections

def main():
   coord_dict = collections.defaultdict(dict)
   coords = []
   contents = sys.stdin.read()
   lines = contents.split('\n')
   for line in lines:
      line = line.strip()
      if len(line) > 0:
         words = line.split(' ')
         axis = words[0]
         value = words[1]
         pad_numbers = words[2:]
         for pad_number in pad_numbers:
            pad_number_for_sorting = "{}".format(pad_number)
            if len(pad_number_for_sorting) == 1:
               if pad_number_for_sorting[0] in ['A', 'B', 'C', 'D']:
                  pad_number_for_sorting = '9' + pad_number_for_sorting
               else:
                  pad_number_for_sorting = '0' + pad_number_for_sorting
            correction_factor = 1.50 if axis == 'y' else 0
            coord_dict[pad_number_for_sorting][axis] = (float(value)-correction_factor)*100
            coord_dict[pad_number_for_sorting]["label"] = pad_number
   #print coord_dict
   sorted_names = coord_dict.keys()
   sorted_names.sort()
   for name in sorted_names:
      value = coord_dict[name]
      print '<smd name="{}" x="{}" y="{}" dx="60" dy="60" layer="1"/>'.format(value["label"], value["x"], value["y"])

if __name__ == "__main__":
   main()
