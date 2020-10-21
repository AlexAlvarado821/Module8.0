import unittest

from more_fun_with_collections import dict_membership as dict


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict.in_dict(1), True)
    def test_in_dict_false(self):
        self.assertEqual(dict.in_dict(-1), False)

if __name__ == '__main__':
    unittest.main()


#Both tests have passed.
