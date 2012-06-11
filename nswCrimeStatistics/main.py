#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

""" main.py: Program Entry Point """

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"

import sys
import html
from crawler import generate_news_list
from crimegmaps import CrimeGMaps

def main():
    """Application entry point"""
    crimeList = generate_news_list()

    for crime in crimeList:
        for idx in range(5):
            print "crime[" + str(idx) +"] : ", str(crime[idx]) #debug string to display progress
        print "----------------------------------------------------------"
    
    header = html.getHeader()
    
    gmap = CrimeGMaps(crimeList)
    
    option = gmap.optionStr()
        
    latlng = gmap.latLngStr()   #get latitude and longitude
    
    places = gmap.placeStr()

    infoWindow = gmap.infoWindowStr()
    
    body = option + latlng + places + infoWindow
    
    footer = html.getFooter()
    
    html.makeHTML(header, body, footer)

    print "NSW crime news page updated"

if __name__ == '__main__':
    status = main()
    sys.exit(status)
