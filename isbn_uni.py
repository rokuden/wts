#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.write("Input isbn code ")
line = sys.stdin.readline()
line = line.rstrip()

print line
keta = len(line)

if keta == 13:
    match = re.search(r'^(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)$',line)
    if match:
        total = int(match.group(1)) * 1 + int(match.group(2)) * 3 + int(match.group(3)) * 1 + int(match.group(4)) * 3 + int(match.group(5)) * 1 + int(match.group(6)) * 3 + int(match.group(7)) * 1 + int(match.group(8)) * 3 + int(match.group(9)) * 1 + int(match.group(10)) * 3 + int(match.group(11)) * 1 + int(match.group(12)) * 3
        #print total
        #print 10 - total % 10
    if 10 - total % 10 == int(match.group(13)):
        print "OK! ISBN-13"
    else:
        print "NG"
elif keta == 10:
    match = re.search(r'^(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)$',line)
    if match:
        total = int(match.group(1)) * 1 + int(match.group(2)) * 2 + int(match.group(3)) * 3 + int(match.group(4)) * 4 + int(match.group(5)) * 5 + int(match.group(6)) * 6 + int(match.group(7)) * 7 + int(match.group(8)) * 8 + int(match.group(9)) * 9
        #print total
        #print total % 11
    if total % 11 == int(match.group(10)):
        print "OK! ISBN-10"
    else:
        print "NG"
else:
    print "NG"
