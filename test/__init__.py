import unittest

from test.test_main import DatabaseTestCase, ParserTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DatabaseTestCase))
    suite.addTest(unittest.makeSuite(ParserTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')