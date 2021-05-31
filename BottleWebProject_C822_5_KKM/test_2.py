import unittest
import Check_Monte_Karlo_NEGR

class Test_test_2(unittest.TestCase):
    def test_correct(self):
        data = ["0..01","FEAS", "4D2AE1","1.D1","-0.012","-12","-0.1"]
        for str in data:
            self.assertFalse(Check_Monte_Karlo_NEGR.check_string(str))

if __name__ == '__main__':
    unittest.main()
