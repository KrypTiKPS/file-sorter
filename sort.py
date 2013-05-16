#!/usr/bin/env python
#File sorter - KrypTiK@p0wersurge.com
import os
import sys

files = []
dirs = []
unknown = []
backups = []

if len(sys.argv) == 2:
	if sys.argv[1] == "--h":
		sys.exit("Use --sort to sort files into appropriate folders")

def sort(dir):
	for x in os.listdir(dir):
		if os.path.isfile(x):
			name, ext = os.path.splitext(x)
			extension = ext[1:]
			if extension[-1:] == "~":
				extension = extension[:-1]
			
			try:
				if x == os.path.basename(__file__):
					continue
				elif x == os.path.basename(__file__)+"~":
					continue
				os.rename(x,extension+"/"+x)
			except OSError:
				os.makedirs(extension) 
				os.rename(x,extension+"/"+x)

def sort_files(dir):
	for x in os.listdir(dir):
		if os.path.isfile(x):
			if x[-1:] == "~":
				backups.append(x)
			else:
				files.append(x)
		elif os.path.isdir(x):
			dirs.append(x)
		else:
			unknown.append(x)

sort_files(".")
for file in files:
	print file + " is a file"

for dir in dirs:
	print dir + " is a directory"

for unkn in unknown:
	print unkn + " is unknown!"

for bckp in backups:
	print bckp + " is a backup file!"

print "\nFiles: " + str(len(files)) + "\nDirectories: " + str(len(dirs)) + "\nUnknown: " + str(len(unknown)) + "\nBackups: " + str(len(backups))

if len(sys.argv) == 2:
	if sys.argv[1] == "--sort":
		print "\nPlease note that this file will not be altered/moved!"
		sort(".")
	else:
		sys.exit("Usage: python "+os.path.basename(__file__)+" <options>\nPlease use --h for help!")
