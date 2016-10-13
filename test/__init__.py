import unittest

from test_main import ParserTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParserTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')