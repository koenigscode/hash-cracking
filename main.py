import sys
import signal
from hashlib import sha1
from time import time
from shuffle_file import shuffle_file

HASH_FILE = "hashes_shuffled"
DICTIONARY_FILE = "words.txt"
LINE_COUNT = False  # count of lines to be processed; False => whole file or till ctrl + c


def stop_program(sig, frame):
    print("--------------------------------------------------\n"
          "{} tried\n{} cracked\ntime: {}s"
          .format(hash_count, len(cracked), time()-start_time))
    sys.exit(0)


def get_additions():
    additions = list("!$?")
    additions.extend(["", 123, 1234, 69, "007"])
    additions.extend([*range(1, 14), *range(2000, 2010), *range(95, 100)])
    # additions.extend(f"0{s}" for s in range(0, 10))
    print("additions: {}\n{}\n"
          "--------------------------------------------------"
          .format(len(additions), ",".join(map(str, additions))))

    return additions


def dictionary_generator(file):
    file.seek(0)
    for line in file:
        line = line.strip("\n")
        yield line
        if line != line.lower():
            yield line.lower()


signal.signal(signal.SIGINT, stop_program)  # handles ctrl + c

if __name__ == "__main__":
    shuffle_file("hashes", "hashes_shuffled")  # shuffles the hash codes
    additions = get_additions()  # additional characters to append to the string
    cracked = {}  # cracked passwords
    hash_count = 0  # read hashes
    start_time = time()

    with open(HASH_FILE) as hash_file, open(DICTIONARY_FILE, "r") as dictionary_file:
        # dictionary_list = [s.strip("\n") for s in dictionary_file]

        hash_list = [next(hash_file)
                     for x in range(LINE_COUNT)] if LINE_COUNT else hash_file

        for hash_val in hash_list:
            # val equals first match found
            # next acts like break in for loop

            val = next((w+str(a) for w in dictionary_generator(dictionary_file)
                        for a in additions if hash_val.strip("\n") == sha1((w+str(a)).encode()).hexdigest()), False)

            if val:
                cracked[hash_val] = val
                print(val)

            hash_count += 1

        stop_program(None, None)
