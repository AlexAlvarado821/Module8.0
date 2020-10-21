
import unittest

from more_fun_with_collections import half_birthday as hb


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(hb.half_birthday(2020, 2, 15), '2020-08-13 00:00:00')


if __name__ == '__main__':
    unittest.main()

#The test passed