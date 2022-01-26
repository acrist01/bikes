import unittest
from app import main

class TestApp(unittest.TestCase):

    def test_app(self):
        testing_data = ['test1.csv', 'test2.csv']

        for test_case in testing_data:
            self.assertEqual(main(f"./tests/{test_case}"),'02:00:00')

if __name__ == '__main__':
    unittest.main()