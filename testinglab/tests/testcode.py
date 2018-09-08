import unittest

from listunit import count_unique

class TestBuiltins(unittest.TestCase):


    """Test some python built-in methods"""





def test_boderline_cases(self):
    list = ["1", "1"]

    self.assertEqual(1, count_unique(list))

def test_typical_case(self):
    list = ["1", "2", "3"]
    self.assertEqual(3, count_unique(list))


def test_impossible_case(self):
    list = [None]
    self.assertEqual(0, count_unique(list))


def test_extreme_case(self):
    list = []
    for i in range(0, 500000):
        list.append(2)
    self.assertEqual(1, count_unique(list))



def test_binary_case(self):
    list = ["1", "2"]
    self.assertEqual(1, test_binary_case(list))
