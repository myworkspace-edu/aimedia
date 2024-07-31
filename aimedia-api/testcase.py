import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def safe_division(self):
        try:
            result = self.a / self.b
            return result
        except ZeroDivisionError:
            return "0"
        except TypeError:
            return ""


if __name__ == '__main__':
    unittest.main()

