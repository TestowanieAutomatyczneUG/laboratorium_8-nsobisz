import unittest
from sample.Age import *
from parameterized import parameterized, parameterized_class


class AgeParameterizedPackage(unittest.TestCase):



    def setUp(self):
        self.tmp = Age()

    @parameterized.expand([
        (1000000000, "zIemIa", 31.69),
        (1231243124, "Mars", 20.74),
        (890245364, "uran", 0.34),
        (0, "Mars", 0)

    ])
    def test_correct_data(self,number,word, expected):
        self.assertEqual(self.tmp.how_old(number,word), expected)

    @parameterized.expand([
        (12000, "asas"),
        (23454, "dsdwk"),
        (34457, {}),
        (346, []),
        (2345, 45),
        (3436, 1.2)

    ])
    def test_wrong_second(self,  number, word):
        self.assertRaises(Exception, self.tmp.how_old, number, word)

    @parameterized.expand([
        (-1, "Ziemia"),
        (-12335, "weNus"),
        (-123243254, "UrAn"),
        ("wefdwef", "Merkury"),
        (1.3, "ziAmIa"),
        ([], "nepTun"),
        ({}, "wenuS"),

    ])
    def test_wrong_first(self, number, word):
        self.assertRaises(Exception, self.tmp.how_old, number, word)

    @parameterized.expand([
        ("sassw", "sfeg"),
        ([], {}),
        ([1, 2, 3], "wdwqdw"),
        (1.2, 234),
        (-20000, "kk"),
        ({}, "kk"),
        ({}, 2.3),
        ("sdsef", {}),
        ("sdawr", [2, 3])

    ])
    def test_wrong_both(self, number, word):
        self.assertRaises(Exception, self.tmp.how_old, number, word)


#zadanie dodatkowe

@parameterized_class(('number', "word", 'expected'), [
    (1000000000, "zIemIa", 31.69),
    (1231243124, "Mars", 20.74),
    (890245364, "uran", 0.34),
    (0, "Mars", 0)
])

class AgeParameterizedPackage_correct_data(unittest.TestCase):
    def setUp(self):
        self.tmp = Age()

    def test_correct_data_2(self):
        self.assertEqual(self.tmp.how_old(self.number, self.word), self.expected)

@parameterized_class(('wrg_number', "wrg_word"), [
    ("sassw", "sfeg"),
    ([], {}),
    ([1, 2, 3], "wdwqdw"),
    (1.2, 234),
    (-20000, "kk"),
    ({}, "kk"),
    ({}, 2.3),
    ("sdsef", {}),
    ("sdawr", [2, 3])
])

class AgeParameterizedPackage_wrong_data(unittest.TestCase):
    def setUp(self):
        self.tmp = Age()

    def test_wrong_data_2(self):
        self.assertRaises(Exception, self.tmp.how_old, self.wrg_number, self.wrg_word)

if __name__ == '__main__':
    unittest.main()

