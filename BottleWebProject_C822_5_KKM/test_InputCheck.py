import unittest
import form_handler

list_input_false = ["asdasd", "001231", "-123", "+-=-=-=-","(123)","+12","+12.2","-14/3", ""]
list_input_true = ["1", "20", "13.2","0.0001","1232"]

class Test_test_1(unittest.TestCase):
    def test_A(self):
        for str in list_input_false:
            self.assertFalse(form_handler.check_input(str))
    def test_B(self):
        for str in list_input_true:
            self.assertTrue(form_handler.check_input(str))

if __name__ == '__main__':
    unittest.main()
