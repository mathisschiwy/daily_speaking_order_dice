import yaml
import unittest
from unittest.mock import patch
from io import StringIO
import functions
from functions import generate_list
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "test_fixture.yaml")
with open(file_path, "r") as config:
    data = yaml.safe_load(config)


class TestInputFunction(unittest.TestCase):
    def test_enter_names(self):
        mock_input = ["Hannes", "Jessica", ""]
        expected_names = ["Henning", "Steffen", "Sarah", "Mathis", "Adrian"]
        todays_participants = functions.build_todays_participants(data)

        with patch('builtins.input', side_effect=mock_input):
            filtered_participants = functions.manual_exclude(todays_participants)

            self.assertEqual(filtered_participants, expected_names)

    def test_exclude_enter_names(self):
        false_name = ["Leon", ""]
        expected_output = "This name is not in the List!\n Enter a name from the following list : Henning, Steffen, Jessica, Sarah, Hannes, Mathis, Adrian"
        todays_participants = functions.build_todays_participants(data)

        with patch('builtins.input', side_effect=false_name), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            functions.manual_exclude(todays_participants)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


class TestGenerateListFunction(unittest.TestCase):
    def test_generate_list_output(self):
        filtered_names = functions.build_todays_participants(data)

        with patch('random.sample', return_value=filtered_names), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
                patch("random.choice", return_value=filtered_names):
            expected_output = "\n".join(filtered_names)

            generate_list(filtered_names)

            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
