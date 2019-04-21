from linear_search import linear_search 
from binary_search
import binary_search 
import unittest

def unitTestSearch(self):
    values = [1, 5, 8, 2, 18, 11]

    indexLinearSearch = self.linear_search(values, 5)
    self.assertEqual(indexLinearSearch, 1)

    indexBinarySearch = self.binary_search(values,5)
    self.assertEqual(indexBinary, 5)

if __name__ == "__main__":
    unittest.main()