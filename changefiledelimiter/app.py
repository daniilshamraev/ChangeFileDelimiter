import argparse
import csv
import os
from typing import Optional

def change_delimiter(input_file: str, output_file: str, old_delimiter: str, new_delimiter: str) -> None:
    """
    Change the delimiter of a file and save the result to a new file.
    """
    if len(old_delimiter) != 1 or len(new_delimiter) != 1:
        raise ValueError("Delimiters must be a single character.")

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file does not exist: {input_file}")

    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
             open(output_file, 'w', newline='', encoding='utf-8') as outfile:

            reader = csv.reader(infile, delimiter=old_delimiter)
            writer = csv.writer(outfile, delimiter=new_delimiter)

            expected_columns = None
            for row in reader:
                if not row:
                    print("Warning: Empty row encountered.")
                    continue
                
                if expected_columns is None:
                    expected_columns = len(row)
                elif len(row) != expected_columns:
                    raise ValueError(f"Inconsistent number of columns in row: {row}")

                writer.writerow(row)

        print(f"Delimiter changed successfully. Output saved to: {output_file}")
    except csv.Error as e:
        print(f"CSV error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description="Change the delimiter of a file.")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to save the output file")
    parser.add_argument("--old_delimiter", type=str, default=",", help="Current delimiter in the file (default: ',')")
    parser.add_argument("--new_delimiter", type=str, default=";", help="Desired delimiter (default: ';')")

    args = parser.parse_args()

    if not args.old_delimiter or not args.new_delimiter:
        print("Error: Delimiters cannot be empty.")
        return

    try:
        change_delimiter(args.input_file, args.output_file, args.old_delimiter, args.new_delimiter)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
