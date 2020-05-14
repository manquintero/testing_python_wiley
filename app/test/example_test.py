import unittest


class MyTestCase(unittest.TestCase):

    def test_assert_rises(self):
        "This is a failed test"
        self.assertRaises(AttributeError, [].get)


if __name__ == '__main__':
    unittest.main()
