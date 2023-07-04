def descramble(lines):
    """
    Reverses the word order of each line. Words are seperated by spaces.
    :param lines:
    :return: lines
    """
    for i, line in enumerate(lines):
        reversed_line = line.rstrip().split(" ")[::-1]
        new_line = " ".join(reversed_line)
        lines[i] = new_line + "\n"
    return lines


if __name__ == '__main__':
    import utils
    from definitions import SCRAMBLED_DATA, DESCRAMBLED_DATA
    input_lines = utils.read_file(SCRAMBLED_DATA / 'letter10_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'letter10_descrambled.txt', output_lines)
