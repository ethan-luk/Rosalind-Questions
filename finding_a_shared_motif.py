from typing import List
from itertools import combinations

def finding_shared_motif(s: List[str]):

    motif = 'A'
    shortest = min(s, key=len)

    s.remove(shortest)

    for i in range(len(shortest)):
        length = 0
        present = True
        while present:
            for sequence in s:
                if shortest[i:i+length] not in sequence or length > 1000:
                    present = False
                    break
            if present:
                motif = max(shortest[i:i+length], motif, key=len)
            length += 1
    return motif


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

    print(finding_shared_motif(sequences))