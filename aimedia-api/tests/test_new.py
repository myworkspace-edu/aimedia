import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = 1 + 1.0
        b = 2
        self.assertEqual(a, b)  # add assertion here


if __name__ == '__main__':
    unittest.main()
