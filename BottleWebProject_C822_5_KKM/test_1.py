import unittest
import Check_Monte_Karlo_NEGR
class Test_test_1(unittest.TestCase):
     def test_correct(self):
        data = ["1","10.8", "444","0.03","1.3","2.222"]
        for str in data:
            self.assertTrue(Check_Monte_Karlo_NEGR.check_string(str))

if __name__ == '__main__':
    unittest.main()

