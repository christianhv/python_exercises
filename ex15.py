#!/usr/bin/env python

from sys import argv
script, filename = argv

txt = open(filename)

print "Here is your fule %r:" % filename
print txt.read()

txt.close()

print "Type the file again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()