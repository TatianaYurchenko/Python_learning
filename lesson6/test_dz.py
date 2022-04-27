import unittest
def compare_two_numbers(a, b):
    if a >= 0 and b >= 0:
        if a >= b:
            return True
        else:
            return False
    else:
        return("can conpare only positive numbers!")

class TestMyCode(unittest.TestCase):
    def setUp(self) -> None:
        print("Starting testing ...")
        print("Set data or something else")


    def test_set_1(self):
        print("a > 0, b > 0")
        a = 4
        b = 3
        self.assertTrue((a >= 0 and b >= 0 and a >= b), "A is not greater then B!")

    def test_set_2(self):
        print("a > 0, b = 0")
        a = 4
        b = 0
        self.assertTrue((a >= 0 and b >= 0 and a >= b), "A is not greater then B!")

    def test_set_3(self):
        print("a = 0, b > 0")
        a = 0
        b = 2
        self.assertFalse((a >= 0 and b >= 0 and a >= b), "A is not greater then B!")

    def test_set_4(self):
        print("a = 0, b = 0")
        a = 0
        b = 0
        self.assertTrue((a >= 0 and b >= 0 and a >= b), "will be faild")

    def test_set_5(self):
        print("a = 0, b > 0")
        a = -2
        b = 2
        self.assertFalse((a >= 0 and b >= 0 and a >= b), "A is not greater then B!")

    def test_set_6(self):
        print("a = 0, b > 0")
        a = 0
        b = -2
        self.assertFalse((a >= 0 and b >= 0 and a >= b), "A is not greater then B!")
        """
        метод который всегда выполняется в конце сценария
        """
    def tearDown(self) -> None:
        print("Clean data or do something else after the test")
        print("Testing is done")
    """
    инструкция для тест ранера
    """

if __name__ == '__main__':
    unittest.main()
