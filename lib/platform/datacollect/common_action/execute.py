#!/usr/bin/python
import sys


file_name = sys.argv[1] + ".txt"
input_file = open(file_name, "r")
server_log = open("/home/admin/TestInput/input.log", "a")
count = 0
for each_line in input_file:
    server_log.write(each_line)
    count += 1
server_log.close()
input_file.close()
print "input " + str(count) + "logs"
print "script execute finish"
