import os
from sys import argv
import gzip

from parser.model import Parser, ProxyLogParser


def support_format(file: str):
    return file.endswith(".gz") or file.endswith(".log")


def read_file(file_name: str):
    if file_name.endswith(".gz"):
        return gzip.open(file_path, 'rt', encoding='utf-8')
    elif file_name.endswith(".log"):
        return open(file_path, 'rt', encoding='utf-8')

    raise TypeError("filename must be a str or bytes object, or a file")


if __name__ == '__main__':
    directory = argv[1]
    parser: Parser = ProxyLogParser()

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # skip unsupported files
            if not support_format(file_path):
                continue

            print('handle file ' + filename)
            with read_file(filename) as log:
                for line in log:
                    parser.parse_line(line)

    parser.write_file(directory + '/result.csv')
