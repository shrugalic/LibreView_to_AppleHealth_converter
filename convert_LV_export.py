#!/usr/local/bin/python3

import os
import pwd
import csv
import codecs
import datetime
from pathlib import Path
import platform

USER_NAME = pwd.getpwuid(os.getuid()).pw_name

# If your LibreView user name differs from the user name on your OS, set it here
LIBRE_VIEW_USER = USER_NAME # 'FirstLast'

# The iCloud (base) directory depends on the platform
ICLOUD_DRIVE_BASE_PATH = '/Library/Mobile Documents'
IS_IOS = platform.machine().startswith("iPhone")
if IS_IOS:
	ICLOUD_DRIVE_DIR = '/private/var/mobile' + ICLOUD_DRIVE_BASE_PATH
else: # Presumably a Mac
	ICLOUD_DRIVE_DIR = str(Path.home()) + ICLOUD_DRIVE_BASE_PATH

# I'm using the 'Pythonista 3' folder in my iCloud drive as base directory:
ICLOUD_DIR = ICLOUD_DRIVE_DIR + '/iCloud~com~omz-software~Pythonista3/Documents'

# Input file: assume the file was exported from LibreView today
INPUT_FILE_NAME = 'LV_' + LIBRE_VIEW_USER + '_Export_' + datetime.date.today().strftime("%d-%m-%Y") + '.csv'


# Input file: iCloud drive on iOS, Downloads folder on macOS
if IS_IOS:
	INPUT_DIR = ICLOUD_DIR
else: # Presumably a Mac
	INPUT_DIR = str(Path.home()) + '/Downloads'
INPUT_FILE_PATH = INPUT_DIR + '/' + INPUT_FILE_NAME

# Output file: always iCloud. The condition is here for cloud deniers ;)
OUTPUT_FILE_NAME = datetime.date.today().isoformat() + "_blood_glucose.csv"
if IS_IOS:
	OUTPUT_FILE_PATH = ICLOUD_DIR + '/' + OUTPUT_FILE_NAME
else: # Presumably a Mac
	OUTPUT_FILE_PATH = ICLOUD_DIR + '/' + OUTPUT_FILE_NAME

codecs.register_error("strict", codecs.ignore_errors)
with codecs.open(INPUT_FILE_PATH, 'rU', 'utf-16-le') as f_in, open(OUTPUT_FILE_PATH, 'w') as f_out:
	input_reader = csv.reader(f_in, delimiter=',')
	writer = csv.writer(f_out, delimiter=',')
	next(input_reader)
	next(input_reader)
	# Input data is expected in mmol/L units, and exported as is
	# If you'd rather use mg/dL, change the column name in the next line to 'Blood Glucose (mg/dL)'
	writer.writerow(['Start', 'Blood Glucose (mmol<180.1558800000541>/L)'])
	for row in input_reader:
		timestamp = row[2]
		# For 12h format, use this
		# iso_timestamp = datetime.datetime.strptime(timestamp, '%m-%d-%Y %I:%M %p').isoformat()
		iso_timestamp = datetime.datetime.strptime(timestamp, '%m-%d-%Y %H:%M').isoformat()
		measurement = row[4] if row[4] else row[5]
		if measurement:
			writer.writerow([iso_timestamp, measurement])
