from descrambler import *


def descramble(lines):
    return lines


if __name__ == '__main__':
    import utils
    from definitions import SCRAMBLED_DATA, DESCRAMBLED_DATA
    input_lines = utils.read_file(SCRAMBLED_DATA / 'final_red_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'final_red_descrambled.txt', output_lines)
    input_lines = utils.read_file(SCRAMBLED_DATA / 'final_blue_scrambled.txt')
    output_lines = descramble(input_lines)
    utils.write_file(DESCRAMBLED_DATA / 'final_blue_descrambled.txt', output_lines)