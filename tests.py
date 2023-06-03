import unittest
from task import conv_num, my_datetime


class TestCase(unittest.TestCase):
    """A required TestCase for basic functional testing"""

    def test1(self):
        self.assertTrue(True)


class FunctionOneTests(unittest.TestCase):
    """A battery of tests designed to check the integrity of
    function conv_num in task.py
    """

    def test1(self):
        """Checks that a non-string input is returned None"""
        value = 123
        self.assertIsNone(conv_num(value), msg='conv_num({})'.format(value))

    def test2(self):
        """Checks that an empty string input is returned None"""
        value = ""
        self.assertIsNone(conv_num(value), msg='conv_num({})'.format(value))

class FunctionTwoTests(unittest.TestCase):
    """
    A battery of tests designed to check the integrity of
    of function my_datetime in task.py
    """

    def test1(self):
        """Checks that a float input is returned None"""
        value = 123.123
        self.assertIsNone(my_datetime(value), msg='my_datetime({})'.format(value))

    def test2(self):
        """Checks that a string input is returned None"""
        value = '123'
        self.assertIsNone(my_datetime(value), msg='my_datetime({})'.format(value))


if __name__ == '__main__':
    unittest.main()
