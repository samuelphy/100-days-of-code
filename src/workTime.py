#!/usr/bin/env python3

import argparse
import sys
import time
import calendar
import collections

arg_names = ['filename', 'key_start', 'key_end', 'key_lunch']
args = dict(zip(arg_names, sys.argv))
Arg_list = collections.namedtuple('Arg_list', arg_names)
args = Arg_list(*(args.get(arg, '00:30') for arg in arg_names)) #Unset args == '00:30'

print(args)

startTime = time.strptime("2000 "+args.key_start, "%Y %H:%M") #Added year 2000 to avoid out of bounds
endTime = time.strptime("2000 "+args.key_end, "%Y %H:%M")
lunchTime = time.strptime("2000 "+args.key_lunch, "%Y %H:%M")

workTime = time.gmtime(calendar.timegm(endTime)-calendar.timegm(startTime)-calendar.timegm(lunchTime))

print(workTime.tm_hour,',', int(workTime.tm_min*100/60), sep = '')
