'''
    @ test case for PlaceSet class
'''

import unittest
from placeset import PlaceSet

class TestPlaceSet(unittest.TestCase):
    place = ""
    def setUp(self):
        self.place = "hornsby"
        pass
    def tearDown(self):
        pass
    
    def test_init(self):
        ps = PlaceSet()
        self.assertIsNotNone(ps.s)
    
    def test_add(self):
        ps = PlaceSet()
        ps.add(self.place)        
        if self.place in ps.s:
            x = True
        else:
            x = False
        self.assertTrue(x)

    def test_has(self):
        ps = PlaceSet()
        self.assertTrue(ps.has(self.place))

    def test_showAll(self):
        ps = PlaceSet()
        ps.showAll()
    
    
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlaceSet)
    unittest.TextTestRunner(verbosity = 2).run(suite)
