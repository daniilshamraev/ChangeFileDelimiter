import os
import unittest
from tempfile import NamedTemporaryFile

from changefiledelimiter.app import change_delimiter


class TestChangeDelimiter(unittest.TestCase):

    def setUp(self):
        """Set up temporary files for testing."""
        self.input_file = NamedTemporaryFile(
            delete=False, mode='w', newline='', encoding='utf-8')
        self.output_file = NamedTemporaryFile(
            delete=False, mode='w', newline='', encoding='utf-8')
        self.input_file.close()
        self.output_file.close()

    def tearDown(self):
        """Clean up temporary files after testing."""
        os.remove(self.input_file.name)
        os.remove(self.output_file.name)

    def write_to_file(self, file_path, content):
        """Helper function to write content to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def read_from_file(self, file_path):
        """Helper function to read content from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def test_change_delimiter_basic(self):
        """Test basic delimiter change."""
        content = "a,b,c\nd,e,f\n"
        self.write_to_file(self.input_file.name, content)

        change_delimiter(self.input_file.name, self.output_file.name, ',', ';')
        result = self.read_from_file(self.output_file.name)

        expected = "a;b;c\nd;e;f\n"
        self.assertEqual(result, expected)

    def test_empty_file(self):
        """Test handling of an empty file."""
        self.write_to_file(self.input_file.name, "")

        change_delimiter(self.input_file.name, self.output_file.name, ',', ';')
        result = self.read_from_file(self.output_file.name)

        self.assertEqual(result, "")

    def test_invalid_delimiters(self):
        """Test invalid delimiters."""
        content = "a,b,c\nd,e,f\n"
        self.write_to_file(self.input_file.name, content)

        with self.assertRaises(ValueError):
            change_delimiter(self.input_file.name,
                             self.output_file.name, '', ';')

        with self.assertRaises(ValueError):
            change_delimiter(self.input_file.name,
                             self.output_file.name, ',', ';;')

    def test_file_not_found(self):
        """Test input file does not exist."""
        with self.assertRaises(FileNotFoundError):
            change_delimiter("non_existent_file.csv",
                             self.output_file.name, ',', ';')

    def test_malformed_csv(self):
        """Test handling of a malformed CSV file."""
        content = "a,b,c\nd,e\n"
        self.write_to_file(self.input_file.name, content)

        with self.assertRaises(ValueError):
            change_delimiter(self.input_file.name,
                             self.output_file.name, ',', ';')


if __name__ == '__main__':
    unittest.main()
