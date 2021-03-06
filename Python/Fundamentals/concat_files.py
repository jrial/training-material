#!/usr/bin/env python

from argparse import ArgumentParser, FileType
from pathlib import Path
import sys


def main():
    arg_parser = ArgumentParser(description='concatenate data files')
    arg_parser.add_argument('-o', dest='output_file', type=FileType('w'),
                            required=True, help='output file')
    arg_parser.add_argument('-p', dest='pattern', required=True,
                            help='file glob pattern')
    options = arg_parser.parse_args()
    path = Path('.')
    is_header_printed = False
    for file_name in path.glob(options.pattern):
        with open(file_name, 'r') as input_file:
            header = input_file.readline()
            if not is_header_printed:
                options.output_file.write(header)
                is_header_printed = True
            for line in input_file:
                if line.strip():
                    options.output_file.write(line)
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
