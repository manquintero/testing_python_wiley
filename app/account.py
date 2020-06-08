""" Dumbest Account """


class Account:
    """ Dummy account holder """

    def __init__(self, handler):
        """ Constructor """
        self.data_interface = handler

    def get_account_id(self):
        """ Queries using the handler """
        return self.data_interface.get_id()

    def get_account_name(self):
        """ Queries using the handler """
        return self.data_interface.get_name()

    def get_account(self):
        """ Always throws error """
        try:
            result = self.data_interface.get()
        except AccountException:
            result = "Connection error occurred"

        return result


class AccountException(Exception):
    """ Dummy Exception """
    pass
