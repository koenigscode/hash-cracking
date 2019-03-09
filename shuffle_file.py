import random


def shuffle_file(input_file_name, output_file_name):
    with open(output_file_name, "w") as file:
        lines = open(input_file_name).readlines()
        random.shuffle(lines)
        file.writelines(lines)
        lines.close()
