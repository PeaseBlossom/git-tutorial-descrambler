def descramble(lines):
    for i, line in enumerate(lines):
        new_line = line.rstrip()
        lines[i] = new_line + "\n"
    return lines


if __name__ == '__main__':
    import utils
    from definitions import SCRAMBLED_DATA, DESCRAMBLED_DATA
    input_lines = utils.read_file(SCRAMBLED_DATA / 'letter5_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'letter5_descrambled.txt', output_lines)
