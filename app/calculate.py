"""My First Class under Test

"""


class Calculate:
    """The simplest broken calculator"""
    def __init__(self):
        pass

    def add(self, first, second):
        """Adds two numbers"""
        if isinstance(first, int) and isinstance(second, int):
            return first + second
        raise TypeError("Invalid type: {} and {}".format(type(first), type(second)))

    def subtract(self, first, second):
        """Adds two numbers"""
        if isinstance(first, int) and isinstance(second, int):
            return first - second
        raise TypeError("Invalid type: {} and {}".format(type(first), type(second)))


if __name__ == '__main__':  # pragma: no cover
    pass
