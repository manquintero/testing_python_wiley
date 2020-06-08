"""My first unit tests

"""
import unittest

from app.calculate import Calculate


class TestCalculate(unittest.TestCase):
    """Unit Test for a simple calculator"""

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        self.calculator = Calculate()

    def test_add_method_return_correct(self):
        """ Test the happy path, sum of two integers """
        self.assertEqual(4, self.calculator.add(2, 2))

    def test_add_method_return_failure(self):
        """Check for a false sum"""
        self.assertNotEqual(4, self.calculator.add(2, 3))

    def test_add_method_raises_typeerror_if_no_first_int(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.add, "Hello", 4)

    def test_add_method_raises_typeerror_if_no_second_int(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.add, "Hello", 4)

    def test_add_method_raises_typeerror_if_not_int(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.add, "Hello", "World")

    def test_add_method_raises_typeerror_if_none(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.add)

    def test_subtract_return_correct(self):
        """ Test the happy path, substract of two integers """
        self.assertEqual(4, self.calculator.subtract(10, 6))

    def test_subtract_method_raises_typeerror_if_no_first_int(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.subtract, "Hello", 4)

    def test_subtract_method_raises_typeerror_if_no_second_int(self):
        """Send no integers"""
        self.assertRaises(TypeError, self.calculator.subtract, 4, "Hello")

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
