import unittest
from add import add


class TestAddFunction(unittest.TestCase):
    def test_add_integer(self):
        result = add(2, 3)
        # self.assertEqual(result, expected)用来判断函数输出结果是否和期望结果一致。
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
