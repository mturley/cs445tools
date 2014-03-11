#!/usr/bin/env python

import sys

def main():
  if len(sys.argv) < 3:
    print 'Usage: '+sys.argv[0]+' <input-file> <output-file>'
  input_file = open(sys.argv[1], 'r')
  output_file = open(sys.argv[2], 'w')
  last_id = ''
  for line in input_file:
    id_field = line.split(',')[0]
    if id_field != last_id:
      output_file.write(line)
    last_id = id_field

if __name__ == '__main__':
  main()
