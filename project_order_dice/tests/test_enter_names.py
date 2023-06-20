import unittest
from unittest.mock import patch
from io import StringIO
from functions import exclude_enter_names
from functions import generate_list


class TestInputFunction(unittest.TestCase):
    def test_enter_names(self):
        names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
        mock_input = ["Hannes", "Jessica", "Henning", "Charlie", ""]
        expected_names = ["Mathis", "Sarah", "Steffen"]

        with patch('builtins.input', side_effect=mock_input):
            exclude_enter_names(names)

            self.assertEqual(names, expected_names)

    def test_exclude_enter_names(self):
        names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
        false_name = ["Leon", ""]
        expected_output = "This name is not in the List!\n Enter a name from the following list : Hannes, Jessica, Henning, Mathis, Sarah, Steffen"

        with patch('builtins.input', side_effect=false_name), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            exclude_enter_names(names)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


class TestGenerateListFunction(unittest.TestCase):
    def test_generate_list_output(self):
        names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]

        with patch('random.sample', return_value=names), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
                patch("random.choice", return_value=names):
            expected_output = "\n".join(names)

            generate_list(names)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
