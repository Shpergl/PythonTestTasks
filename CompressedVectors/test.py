import unittest
from compressed_lists import *


class TestScalarMultiply(unittest.TestCase):
    lst1 = [1,4,3,4,5,3,1,5]
    lst2 = [3,5,4,6,5,5]
    lst3 = [1,2,3,'4']

    def test_check_lst_length(self):
        res = check_lst_len(self.lst1)
        self.assertEqual(res, 16)

    def test_check_number_is_not_int(self):
        self.assertRaises(Exception, check_lst_len(self.lst3))

    def test

if __name__ == '__main__':
    unittest.main()
