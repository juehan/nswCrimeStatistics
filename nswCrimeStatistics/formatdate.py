#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

"""formatdate.py: formatting calendar date format into SQLite date format """

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"

'''
This module is to translate published date format like below
    "Friday, 17 February 2012 02:13:44 PM"
into SQLite supportive date format like below
    "2012-02-17 02:13:44"
    "YYYY-MM-DD HH:MM:SS"

See below link for SQLite supportive date format
http://www.sqlite.org/lang_datefunc.html

'''

def formatDate(d):
    dPartitioned = d.partition(",")
    dateList = dPartitioned[2].split()
    day = dateList[0]
    month_dict = {"January":"01", 
                  "February":"02", 
                  "March":"03",
                  "April":"04", 
                  "May":"05", 
                  "June":"06",
                  "July":"07", 
                  "August":"08", 
                  "September":"09",
                  "October":"10", 
                  "November":"11", 
                  "December":"12"}

    def toMonthNum(name):
        return month_dict[name]

    month = toMonthNum(dateList[1])
    year = dateList[2]
    time = dateList[3]
    return year+"-"+month+"-"+day+" "+time

'''
#test
d = "Friday, 17 February 2012 02:13:44 PM"; 
print formatDate(d)

'''

