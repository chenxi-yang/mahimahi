'''
Read from the (bw, loss, delay) sequence file and update the file to mahimahi
'''

import os

SEQ_FILE_DIR = "/newhome/mahimahi/test/sequence_generator/sequence_files"
PIPE_PATH = "/newhome/adversary_update"
if not os.path.exists(PIPE_PATH):
    os.mkdir(PIPE_PATH)

def read_seq(seq_name):
    file_path = os.path.join(SEQ_FILE_DIR, "sequence_" + seq_name + ".txt")
    seq_f = open(file_path, "r")
    seq_f.readline() # skip the first line
    seq_list = []
    for line in seq_f.readlines():
        bw, loss, delay = line[:-1].split()
        bw, loss, delay = float(bw), float(loss), float(delay)
        seq_list.append((bw, loss, delay))
    seq_f.close()
    return seq_list


def write_pipe(seq_name):
    pipe_file = os.path.join(PIPE_PATH, f"pipe_{seq_name}.txt")
    seq = read_seq(seq_name)
    while True:
        for (bw, loss, delay) in seq:
            sleep(0.1) # sleep for 100ms
            # write to the adversary_update_pipe
            # assume the reading/checking interval in the shell is less than 100ms
            pipe_f = open(pipe_file, "w")
            pipe_f.write(f"{bw},{loss},{delay}\n")
            pipe_f.close()


if __name__ == "__main__":
    # seq_name
    seq_name = "test_1" # maps to the sequence file in /mahimahi/test/sequence_generator/sequence_files/sequence_test_1.txt
    write_pipe(seq_name)