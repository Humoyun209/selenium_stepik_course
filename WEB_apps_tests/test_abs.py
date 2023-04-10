import unittest


def palindrome(num):
    return num == num[::-1]


class TestNumber(unittest.TestCase):
    def test_abs(self):
        self.assertEqual(abs(-42), 42, 'Число не равен к 42')

    def test_palindrome(self):
        self.assertEqual(palindrome('11511'), True, 'Число не палиндром')


if __name__ == '__main__':
    unittest.main()