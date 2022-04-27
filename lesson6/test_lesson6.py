import unittest
class TestMyCode(unittest.TestCase):

    def setUp(self) -> None:   # метод который всегда выполняется в начале сценария
        print("Starting testing ...")
        print("Set data or something else")


    def test_is_a_greater_than_b(self):
        print("test _is_a_greater_than_b")
        a = 4
        b = 3
        self.assertTrue(a > b, "A is not greater then B!")
    def test_x_is_equal_to_y(self):
        print("test_x_is_equal_to_y")
        x = 3
        y = 3
        self.assertTrue(x == y, "X is not equal Y!")
        # or
        # self.assertEqual(x,y)

    def tearDown(self) -> None: # метод который всегда выполняется в конце сценария
        print("Clean data or do something else after the test")
        print("Testing is done")


if __name__ == '__main__': # инструкция для тест ранера
    unittest.main()

