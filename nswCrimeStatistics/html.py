#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

"""html.py: provide HTML header and footer to construct crime report webpage """

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"


import nswtime

_TIME = nswtime.gettime() #get 

_HEADER = '<!DOCTYPE html><html><head><title>NSW Crime Report</title>\n\
<meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\"/>\n\
<style type=\"text/css\">\n\
html { height: 100% }\n\
body { height: 90%; margin: 5; padding: 5 }\n\
#map_canvas { height: 100% }\n\
</style>\n\
<script type=\"text/javascript\"\n\
    src="http://maps.googleapis.com/maps/api/js?key=AIzaSyDUWg0EnNMSjHXKFMXMRiHR_V3enb5qMho&sensor=false\">\n\
</script>\n\
<script type=\"text/javascript\">\n'

_FOOTER = '<body onload=\"initialize()\">\n\
            <div id=\"map_canvas\" style=\"width:100%; height:100%\"></div>\n\
            <br>Refer to <a href="readme.htm">README</a> page for some details of this app.\n\
	        <br>Last updated: ' + \
            _TIME + \
            ' (UTC/GMT+10 hours, EDT, Sydney/Australia)\n\
          </body></html>'

def getHeader():
    """ return header part of HTML """
    return _HEADER

def getFooter():
    """ return footer part of HTML"""
    return _FOOTER

def makeHTML(header, body, footer):
    """ create html file and compose it with given header, body and footer """
    f = open("crimenews.html", "w")
    f.write(header+body+footer)
