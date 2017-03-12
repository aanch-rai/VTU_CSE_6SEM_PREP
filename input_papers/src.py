import re
import sys
import os
import filemapper as fm


def open_fun(sub, unit):
            sub_dir = fm.load(sub,'w') # fm.load('sub','w') will open in write mode, loads all files in the directory
            #print sub_dir --shows the files from the given directory
            for f in sub_dir:
                print f
                #print os.path.realpath(f) 
                to_open = open(f)
                to_read = to_open.read()
                regex = re.escape(unit) + ur"[a-z]\..*" #specifies which unit to select
                unit_list = re.findall(regex, to_read) #returns the list containing the regex
                for i in range(len(unit_list)):
                    print unit_list[i]
                print "\n"
                print "*"*130


print "Here are the list of papers available :- "
print "->1 for ME\n->2 for CD\n-> 3 for CN"
ch = raw_input("Enter your choice:")
if ch=='ME':
	unit = raw_input("Please enter which unit you would like to refer to:")
        print "\n"
        print "*"*130
        open_fun(ch, unit)
elif ch == "CD":
	unit = raw_input("Please enter which unit you would like to refer to:")
        print "\n"
        print "*"*130
        open_fun(ch, unit)
else:
	unit = raw_input("Please enter which unit you would like to refer to:")
        print "\n"
        print "*"*130
        open_fun(ch, unit)
