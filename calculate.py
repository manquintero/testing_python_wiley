class Calculate:
    """The simplest broken calculator

    """
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y


if __name__ == '__main__':
    calculator = Calculate()
    result = calculator.add(2, 2)
    print(result)
