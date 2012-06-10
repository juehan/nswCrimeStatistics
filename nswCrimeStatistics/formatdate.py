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
    l = dPartitioned[2].split()
    day = l[0]
    month_dict = {"January":"01", "February":"02", "March":"03",
                  "April":"04", "May":"05", "June":"06",
                  "July":"07", "August":"08", "September":"09",
                  "October":"10", "November":"11", "December":"12"}

    def toMonthNum(name):
        return month_dict[name]

    month = toMonthNum(l[1])
    year = l[2]
    time = l[3]
    return year+"-"+month+"-"+day+" "+time

'''
#test
d = "Friday, 17 February 2012 02:13:44 PM"; 
print formatDate(d)

'''

