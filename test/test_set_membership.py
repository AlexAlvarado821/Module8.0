import unittest

from more_fun_with_collections import set_membership



class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set([1, 2, 3, 4, 5], 4), True)

    def test_in_set_false(self):
        self.assertEqual(set_membership.in_set([1, 2, 3, 4, 5], 6), False)



if __name__ == '__main__':
    unittest.main()

# tests have all passed

