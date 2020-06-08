""" My First Mock """
import unittest

from mock import Mock


class TestMocking(unittest.TestCase):
    """ My First Mock """
    def test_mock_method_returns(self):
        """ Simple Hello-Work Mock """
        my_mock = Mock()
        my_mock.my_method.return_value = "hello"
        self.assertEqual("hello", my_mock.my_method())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
