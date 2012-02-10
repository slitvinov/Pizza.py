#!/usr/bin/python

# Script:  dview.py
# Purpose: launch vcr tool on LAMMPS dump files
# Syntax:  dview.py dump.1 dump.2 ...
#          files = one or more dump files
# Example: dview.py dump.*
# Author:  Steve Plimpton (Sandia)

# main script

if len(argv) < 2:
  raise StandardError, "Syntax: dview.py dump.1 ..."

files = ' '.join(argv[1:])

d = dump(files)
g = gl(d)
v = vcr(g)
