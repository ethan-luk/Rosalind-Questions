from typing import List

def finding_shared_motif(s: List[str]):
    pass


if __name__ == '__main__':
    path ='data/rosalind_lcsm.txt'

    with open(path, 'r') as f:
        data = f.readlines()

    sequences = []
    current_seq = ''
    for index, line in enumerate(data):
        if line.startswith('>') and index != 0:
            sequences.append(current_seq)
            current_seq = ''
        else:
            current_seq = current_seq + line.strip()

    finding_shared_motif(sequences)