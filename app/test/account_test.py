""" Simple Test """
import unittest

from mock import Mock

from app.account import Account, AccountException


class MyTestCase(unittest.TestCase):
    """ Simple Test """

    def setUp(self):
        """ Hook method for setting up the test fixture before exercising it. """
        self.account_data = {"id": "1", "name": "test"}
        mock_data_interface = Mock()
        mock_data_interface.get_id.return_value = '1'
        mock_data_interface.get_name.return_value = 'test'
        mock_data_interface.get.side_effect = AccountException()
        self.account = Account(mock_data_interface)

    def test_account_returns_data_for_id(self):
        """ Simple Test for ID """
        self.assertEqual(self.account_data["id"], self.account.get_account_id())

    def test_account_returns_data_for_name(self):
        """ Simple Test for NAME """
        self.assertEqual(self.account_data["name"], self.account.get_account_name())

    def test_account_when_connect_exception_raised(self):
        """ Raises Exception """
        self.assertEqual("Connection error occurred", self.account.get_account())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
