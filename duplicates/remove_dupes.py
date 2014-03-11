#!/usr/bin/env python

import sys

def main():
  if len(sys.argv) < 3:
    print 'Usage: '+sys.argv[0]+' <input-file> <output-file>'
  input_file = open(sys.argv[1], 'r')
  output_file = open(sys.argv[2], 'w')
  last_id = ''
  total_count = 0
  dupe_count = 0
  for line in input_file:
    id_field = line.split(',')[0]
    if id_field != last_id:
      output_file.write(line)
    else:
      dupe_count += 1
      print 'REMOVED DUPLICATE: "'+line+'"'
    last_id = id_field
    total_count += 1
  print 'Complete! Removed '+str(dupe_count)+' duplicate-ID rows out of '+str(total_count)+' total rows.'
  print str(total_count - dupe_count) +' lines were copied to '+sys.argv[2]+'.'

if __name__ == '__main__':
  main()
