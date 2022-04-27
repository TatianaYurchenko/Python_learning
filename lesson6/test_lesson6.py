"""
Пример файла содержащего юнит тесты по класической схеме, состоящей из 3-х частей
"""
import unittest

class TestMyCode(unittest.TestCase):
    """
    метод который всегда выполняется в начале сценария
    """

    def setUp(self) -> None:
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

