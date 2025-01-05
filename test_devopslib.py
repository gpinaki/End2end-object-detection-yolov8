import unittest
from unittest.mock import patch
from devopslib import randomfruits


class TestFruitFunction(unittest.TestCase):
    
    @patch('fruit.choices')  # Replace 'your_module' with the actual module name
    def test_fruit(self, mock_choices):
        # Mock the return value of choices to ensure predictable output
        mock_choices.return_value = ['apple']
        
        result = randomfruits.fruit()
        self.assertEqual(result, 'apple')

if __name__ == '__main__':
    unittest.main()