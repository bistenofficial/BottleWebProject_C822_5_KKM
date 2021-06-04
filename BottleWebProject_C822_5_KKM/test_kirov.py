import unittest
import check

list_input_false = ["fdsdfsegfdgb","0222","-0.22","           0.22","(1.2)","4.5"]
list_input_true = ["1.0", "0.22", "0.0002","0.0001","0.3333221"]

class Test_test_1(unittest.TestCase):
    def test_A(self):
        for str in list_input_false:
            self.assertFalse(check.fieldTest(str))
    def test_B(self):
        for str in list_input_true:
            self.assertTrue(check.fieldTest(str))

if __name__ == '__main__':
    unittest.main()

