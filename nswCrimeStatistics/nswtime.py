#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python


"""nswtime.py: Get Sydney / Australia's local time"""

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"

import os
import time
from time import strftime
import sys

def gettime():
	"""returns Australia/Sydney time"""
	os.environ['TZ'] = 'Australia/Sydney'   #change timezone
	if not sys.platform == "win32":
		time.tzset()    # this is not supported at Windows Environment
	return strftime("%Y-%m-%d %H:%M:%S")

