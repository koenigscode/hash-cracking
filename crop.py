with open("./644_asylum_found_hash_hex (1).txt", "r") as input_file:
    with open("./hashes", "w") as output_file:
        output_file.write("\n".join([s[:s.index(":")] for s in input_file]))
