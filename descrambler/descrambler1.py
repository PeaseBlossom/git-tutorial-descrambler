def descramble(lines):
    """
    Descrambles the given lines of text: replaces all 'y' with 'o' and vice versa.
    :param lines: list of lines of text
    :return: descrambled lines of text
    """
    for i, line in enumerate(lines):
        new_line = line.rstrip()

        # replace y with o and o with y
        new_line = new_line.replace('y', '*').replace('o', 'y').replace('*', 'o')

        lines[i] = new_line + "\n"
    return lines


if __name__ == '__main__':
    import utils
    from definitions import SCRAMBLED_DATA, DESCRAMBLED_DATA
    input_lines = utils.read_file(SCRAMBLED_DATA / 'letter1_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'letter1_descrambled.txt', output_lines)
