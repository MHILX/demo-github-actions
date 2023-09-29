from main import return_backwards_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    def test_hello_name(self):
        name = 'mohammed'
        self.assertEqual(hello_name(name), f'Hello, {name}!')

if __name__ == '__main__':
    unittest.main()