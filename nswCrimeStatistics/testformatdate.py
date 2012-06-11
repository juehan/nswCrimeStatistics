#!/usr/bin/eval PYTHONPATH=/home/nswcrime/modules python

import unittest
from formatdate import formatDate

class TestFormatDate(unittest.TestCase):
    dates = ['Friday, 17 February 2012 02:13:44 PM',
             'Monday, 23 November 2011 08:23:11 AM',
             'Fri, 30 July 2011 00:59:22 ',
             'Tuesday, 17 January 2010 12:11:31 2qq',
             'Monday, 17 October 2011 14:32:14 am',
             'Wed, 17 April 2011 23:44:41 AM',
             'Sat, 17 May 2011 11:16:54',
             'Sunnnnnnnnnnnnn, 17 March 2012 10:56:11 AM',
             'afsadasd, 17 August 2013 09:42:33 AM',
             '13243, 17 December 2009 19:31:54 PM']
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_formatDate(self):
        for d in self.dates:
            print formatDate(d)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFormatDate)
    unittest.TextTestRunner(verbosity=2).run(suite)
