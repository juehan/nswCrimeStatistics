#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

"""placeset.py: create place table in SQLite"""

__author__ = "John (Ju-han) Lee"
__copyright__ = "Copyright 2012, nswCrimeStatistics Project"
__credits__ = "John (Ju-han) Lee"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "John (Ju-han) Lee"
__email__ = "to.johnny.lee@gmail.com"
__status__ = "Experimental"

'''
Store to keep location on set container
1. check file whether already exist
2. if so, open file, unpickle and load it to set
2-1. if not, create empty set and pickle it and store as file

'''

import os
import pickle

class PlaceSet:
    
    filename = "pset.p"
    filemode = "r+"
    def __init__(self):
        if not os.path.isfile(self.filename):   #fixme: if file is not exist, replace it from backup
            self.f = open(self.filename, "w")
            l = ['waitara']
            s = set(l)
            pickle.dump(s, self.f)
            self.f.close()
        else:
            self.f = open(self.filename, self.filemode)
            self.s = pickle.load(self.f)
            self.f.close()        
        
    def add(self, place):
        self.s.add(place)
        self.f = open(self.filename, self.filemode)
        pickle.dump(self.s, self.f)
        self.f.close()
        
    def has(self, place):
        if place in self.s:
            return True
        return False
    
    def showAll(self):
        for place in self.s:
            print place
