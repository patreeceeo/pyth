import unittest
import pyth
import os

class TestCase(unittest.TestCase):

    def test_unix(self):
        self.assertEqual(pyth.unix('~'), os.path.expanduser('~')) 
        self.assertEqual(pyth.unix('/abs/path'), os.sep + os.path.join('abs', 'path'))
        self.assertEqual(pyth.unix('rel/path'), os.path.join('rel', 'path'))
        self.assertEqual(pyth.unix('rel/path/'), os.path.join('rel', 'path', ''))
        self.assertEqual(pyth.unix('~/abs/path'), os.path.join(os.path.expanduser('~'), 'abs', 'path')) 

if __name__ == '__main__':
    unittest.main()
