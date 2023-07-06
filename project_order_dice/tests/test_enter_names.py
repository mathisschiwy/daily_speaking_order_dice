
import unittest
from unittest.mock import patch
from io import StringIO

import functions
from functions import generate_list


class TestInputFunction(unittest.TestCase):
    def test_enter_names(self):
        mock_input = ["Hannes", "Jessica", ""]
        expected_names = ["Henning", "Steffen", "Sarah", "Mathis", "Adrian"]

        with patch('builtins.input', side_effect=mock_input):
            participants = functions.build_todays_participants()

            self.assertEqual(participants, expected_names)

    def test_exclude_enter_names(self):
        false_name = ["Leon", ""]
        expected_output = "This name is not in the List!\n Enter a name from the following list : Henning, Steffen, Jessica, Sarah, Hannes, Mathis, Adrian"

        with patch('builtins.input', side_effect=false_name), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            functions.build_todays_participants()

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


class TestGenerateListFunction(unittest.TestCase):
    def test_generate_list_output(self):
        filtered_names = ["Steffen", "Jessica", "Sarah", "Hannes", "Mathis", "Adrian"]

        with patch('random.sample', return_value=filtered_names), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
                patch("random.choice", return_value=filtered_names):
            expected_output = "\n".join(filtered_names)

            generate_list(filtered_names)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


