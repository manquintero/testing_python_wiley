import unittest

from calculate import Calculate


class TestCalculate(unittest.TestCase):
    """

    """

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        self.calculator = Calculate()

    def test_add_method_return_correct(self):
        self.assertEqual(4, self.calculator.add(2, 2))

    def test_add_method_return_failure(self):
        self.assertNotEqual(4, self.calculator.add(2, 3))


if __name__ == '__main__':
    unittest.main()
