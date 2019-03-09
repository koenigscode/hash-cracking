with open("words.txt") as input_file, open("words", "w") as output_file:
    a = input_file.readlines()
    print(len(a[0].replace("\r", "")))
