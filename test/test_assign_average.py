import unittest

from more_fun_with_collections import assign_average as grade
class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(grade.switch_average('A'), 'You entered an A!')

    def test_b(self):
        self.assertEqual(grade.switch_average('B'), 'You entered a B!')

    def test_c(self):
        self.assertEqual(grade.switch_average('C'), 'You entered a C!')

    def test_d(self):
        self.assertEqual(grade.switch_average('D'), 'You entered a D!')

    def test_f(self):
        self.assertEqual(grade.switch_average('F'), 'You entered a F!')

    def test_invalid_value(self):
        self.assertEqual(grade.switch_average('R'), "This is not a valid grade")


if __name__ == '__main__':
    unittest.main()


#all tests have passed