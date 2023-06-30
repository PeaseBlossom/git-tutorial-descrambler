import os


def read_file(filename):
    """
    Read a text file.
    :param filename: path to the text file
    :return: list of lines from the text file
    """
    with open(filename) as f:
        lines = f.readlines()
    return lines


def write_file(filename, lines):
    """
    Create a file with text.
    :param filename: path to the text file
    :param lines: list of lines for the text file
    :return:
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.writelines(lines)
