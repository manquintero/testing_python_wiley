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
