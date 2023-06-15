import unittest
from unittest.mock import patch
from io import StringIO
from functions import enter_names
from functions import generate_list

class TestInputFunction(unittest.TestCase):
    def test_input(self):
        names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
        mock_input = ["Hannes", "Jessica", "Henning", "Charlie", ""]
        expected_names = ["Mathis", "Sarah", "Steffen"]

        with patch('builtins.input', side_effect=mock_input):

            enter_names(names)

            self.assertEqual(names, expected_names)

class TestGenerateListFunction(unittest.TestCase):
    def test_generate_list_output(self):
        names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]

        with patch('random.sample', return_value=names), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            expected_output = "\n".join(names)

            generate_list(names)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)



