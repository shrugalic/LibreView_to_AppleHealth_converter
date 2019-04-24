#!/usr/local/bin/python3

import csv
import codecs
import datetime
from pathlib import Path
import platform

# Your LibreView user name
LIBRE_VIEW_USER = 'FirstLast'

# Use iCloud drive by default. Set to False to use local storage (next to this script) instead
USE_ICLOUD_DRIVE = True

# Home directory. /Users/your_short_name on a Mac, something in /var/mobile/… in iOS
HOME = str(Path.home())

if platform.system() != 'Darwin':
	print('Only iOS and macOS are supported. Exiting.')
	#import sys
	sys.exit(1)

IS_IOS = platform.machine().startswith("iPhone")

if USE_ICLOUD_DRIVE:
	
	# Set iCloud drive directory
	if IS_IOS:
		FS_ROOT_DIR = '/private/var/mobile'
	else: # Mac
		FS_ROOT_DIR = HOME
	
	# Local copy of iCloud drive
	ICLOUD_DRIVE_DIR = FS_ROOT_DIR + '/Library/Mobile Documents/'
	
	# I'm using the 'Pythonista 3' folder in my iCloud drive as base directory:
	BASE_DIR = ICLOUD_DRIVE_DIR + '/iCloud~com~omz-software~Pythonista3/Documents'

else: # Local storage
	
	if IS_IOS:
		# Use the home directory of the app that runs this script (such as Pythonista)
		BASE_DIR = HOME
	else: # Mac
		# Assume the CSV to import is located next to this script
		import os
		BASE_DIR = os.path.dirname(__file__) # Directory this script is in

INPUT_FILE_NAME = BASE_DIR + '/LV_' + LIBRE_VIEW_USER + '_Export_' + datetime.date.today().strftime("%m-%d-%Y") + '.csv'
OUTPUT_FILE_NAME = BASE_DIR + '/' + datetime.date.today().isoformat() + "_blood_glucose.csv"

codecs.register_error("strict", codecs.ignore_errors)
with codecs.open(INPUT_FILE_NAME, 'rU', 'utf-16-le') as f_in, open(OUTPUT_FILE_NAME, 'w') as f_out:
	input_reader = csv.reader(f_in, delimiter=',')
	writer = csv.writer(f_out, delimiter=',')
	next(input_reader)
	next(input_reader)
	# Input data is expected in mmol/L units, and exported as is
	# If you'd rather use mg/dL, change the column name in the next line to 'Blood Glucose (mg/dL)'
	writer.writerow(['Start', 'Blood Glucose (mmol<180.1558800000541>/L)'])
	for row in input_reader:
		timestamp = row[2]
		iso_timestamp = datetime.datetime.strptime(timestamp, '%m-%d-%Y %I:%M %p').isoformat()
		measurement = row[4] if row[4] else row[5]
		if measurement:
			writer.writerow([iso_timestamp, measurement])
