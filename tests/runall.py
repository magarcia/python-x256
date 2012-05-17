import unittest

import test_x256

def get_suite():
    suite_x = unittest.defaultTestLoader.loadTestsFromModule(test_x256)
    suite = unittest.TestSuite([suite_x])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='get_suite')