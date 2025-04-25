import unittest
from io import StringIO
import sys
import project_code

class TestSumOfSquares(unittest.TestCase):
    
    def setUp(self):
        self.saved_stdout = sys.stdout  
        self.saved_stdin = sys.stdin    

    def tearDown(self):
        sys.stdout = self.saved_stdout  
        sys.stdin = self.saved_stdin    

    def test_sum_of_squares(self):
        test_input = '''2
3
1 2 3
4
-1 -2 3 4
'''

        expected_output = '''14
25
'''

        # Redirect stdin to simulate user input
        sys.stdin = StringIO(test_input)
        
        # Redirect stdout to capture output
        sys.stdout = StringIO()

        project_code.main()

        result = sys.stdout.getvalue()

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()


