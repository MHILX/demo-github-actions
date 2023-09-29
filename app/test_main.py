import unittest
from main import hello, hello_name

class TestMain(unittest.TestCase):
    def test_hello_name(self):
        name = 'mohammed'
        result = hello_name(name)
        print(result)
        self.assertEqual(result, f'Hello, {name}!')

if __name__ == '__main__':
    unittest.main()