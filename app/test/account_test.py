""" Simple Test """
import unittest

from mock import Mock

from app.account import Account


class MyTestCase(unittest.TestCase):
    """ Simple Test """

    def setUp(self):
        """ Hook method for setting up the test fixture before exercising it. """
        self.account_data = {"id": "1", "name": "test"}
        mock_data_interface = Mock()
        mock_data_interface.get_id.return_value = '1'
        mock_data_interface.get_name.return_value = 'test'
        self.account = Account(mock_data_interface)

    def test_account_returns_data_for_id(self):
        """ Simple Test for ID """
        self.assertEqual(self.account_data["id"], self.account.get_account_id())

    def test_account_returns_data_for_name(self):
        """ Simple Test for NAME """
        self.assertEqual(self.account_data["name"], self.account.get_account_name())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
