def descramble(lines):
    """
    Descrambles the input lines: swaps out the "ba" and "de" in each line and vice versa.
    :param lines:
    :return:
    """
    for i, line in enumerate(lines):
        new_line = line.rstrip()

        # Replace "ba" with "de" and vice versa
        new_line = new_line.replace("ba", "*").replace("de", "ba").replace("*", "de")

        lines[i] = new_line + "\n"
    return lines


if __name__ == '__main__':
    import utils
    from definitions import SCRAMBLED_DATA, DESCRAMBLED_DATA
    input_lines = utils.read_file(SCRAMBLED_DATA / 'letter6_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'letter6_descrambled.txt', output_lines)
