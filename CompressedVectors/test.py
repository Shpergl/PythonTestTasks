import unittest
from compressed_lists import *


class TestScalarMultiply(unittest.TestCase):
    lst1 = [1,4,3,4,5,3,1,5]
    lst2 = [3,5,4,6,5,5]
    

    def test_check_lst_length(self):
        for lst in [self.lst1, self.lst2]:
            res = check_lst_len(lst)
            self.assertEqual(res, 16)

    def test_set_next_lst(self):
        res = set_next_lst(self.lst1, self.lst2, 0,0) 
        self.assertEqual(res, ([1,4], [3,5], 2,2))

    def test_scalar_multiply_lst(self):
        res = scalar_multiply_lst(self.lst1, self.lst2)
        self.assertEqual(res, 142)

if __name__ == '__main__':
    unittest.main()
