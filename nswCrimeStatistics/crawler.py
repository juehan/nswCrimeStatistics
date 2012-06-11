# -*- coding:utf-8 -*-
#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

"""crawler.py: Web crawler and post-processor to retrieve NSW crime report from NSW Police website 
    This is wrapper for geopy library and use BeautifulSoup to process HTML soup.
"""

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"

import urllib2

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup # BeautilSoup4.x
from geopy import geocoders
import time
import re


def has_dash(mystr):
    '''check whether string has dash ''' 
    location = mystr.find('-')
    if location is not -1:
        if mystr[location+1] == " ":
            return True
        return False

def is_valid_location(rawlocation):
    '''return false if location is longer than 3 words'''
    locationlist =  rawlocation.split(' ')
    if len(locationlist) > 2:
        return False
    else:
        return True
  
# \u2010 : HYPHEN
# \u2013 : EN DASH
# \u2014 : EM DASH
def analyze_title(title):
    ''' Analyze title'''
    hasdash = has_dash(title)
    if hasdash:
        location = title.find('-')
        strcrime = title[:location - 1]
        if is_valid_location(title[location + 2:]):
            strlocation = title[location + 2:] + ", NSW, Australia"
        else:
            strlocation = ""
        return (strcrime, strlocation)
    else:
        return ("", "")

  
def get_latlng_list(location):
    '''   get latitude and longitude    '''
    latlng = []
    gmaps = geocoders.Google(resource = 'maps')
  
    try:    
        places, (lat, lng) = gmaps.geocode(location)
        time.sleep(0.1)
        latlng.append("%.5f" % lat)
        latlng.append("%.5f" % lng)
    except Exception as ex:
#    x = "Didn't find exactly one placemark!"
#    if str(e).find(x) >= 0:
#      places, (lat, lng) = g.geocode(location, exactly_one=False)
#      #places = g.geocode(location, exactly_one=False)
#      time.sleep(0.1)
#      latlng.append("%.5f" % places[1][0])
#      latlng.append("%.5f" % places[1][1])
#      log = open('logfile.txt', 'a')
#      s = 'location: {0}, Exception: {1}'.format(location, e)
#      log.write('%s\n' %s)
#      log.close()
#    else:
#      log = open('logfile.txt', 'a')
#      s = 'location: {0}, Exception: {1}'.format(location, e)
#      log.write('%s\n' %s)
#      log.close()  
        log = open('logfile.txt', 'a')
        ss_ = 'location: {0}, Exception: {1}'.format(location, ex)
        log.write('%s\n' %ss_)
        log.close()

    return latlng
  

NEWS_SITE = 'http://m.police.nsw.gov.au/news'

def generate_news_list():
    '''generate news list'''
    html_source = urllib2.urlopen(NEWS_SITE)
    soup = BeautifulSoup(html_source.read())
    newslist = []
    for i in range (2, 32):
        htmltext = soup('li')[i]
        weblink = htmltext('a')[0]['href']
        info = htmltext.findAllNext(text = True)
        date = info[2]
        strcrime, strlocation = analyze_title(info[1])
        latlang = get_latlng_list(strlocation)
     
        if strcrime and strlocation and len(latlang) > 0:
            news = []
            if re.search('"', strcrime) or re.search("'", strcrime) :
                strcrime_escaped = re.escape(strcrime)
                news.append(strcrime_escaped)
            else:
                news.append(strcrime)
            news.append(strlocation)
            news.append(weblink)
            news.append(date)
            news.append(latlang)
            newslist.append(news)
    return newslist
