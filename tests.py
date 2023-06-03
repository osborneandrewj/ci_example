import unittest
from task import conv_num


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

    def test3(self):
        """Checks that a double .. string input is returned None"""
        value = "1.0."
        self.assertIsNone(conv_num(value), msg='conv_num({})'.format(value))

    def test4(self):
        """Checks that an invalid character is returned None"""
        value = "99.00G"
        self.assertIsNone(conv_num(value), msg='conv_num({})'.format(value))

    def test5(self):
        """Checks that string '123' is returned int 123"""
        value = "123"
        expected = 123
        self.assertEqual(conv_num(value), expected,
                         msg='conv_num({})'.format(value))

    def test6(self):
        """Checks that string '-123' is returned negative int -123"""
        value = "-123"
        expected = -123
        self.assertEqual(conv_num(value), expected,
                         msg='conv_num({})'.format(value))

    def test7(self):
        """Checks that string '0.45' is returned float 0.45"""
        value = "0.45"
        expected = 0.45
        self.assertEqual(conv_num(value), expected,
                         msg='conv_num({})'.format(value))


if __name__ == '__main__':
    unittest.main()
