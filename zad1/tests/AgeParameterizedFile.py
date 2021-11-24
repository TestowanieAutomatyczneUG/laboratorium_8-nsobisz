import unittest
from sample.Age import *

class AgeParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/age_data_test")
      tmpFizzBuzz = Age()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp1, inp2, result = int(data[0]), data[1], float(data[2].strip("\n"))
            self.assertEqual(tmpFizzBuzz.how_old(inp1, inp2), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()

