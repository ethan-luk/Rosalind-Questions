from typing import List

def compute_gc(data: List[str]):
    max_subj = ''
    max_gc = 0

    for index, line in enumerate(data):
        if line.startswith('>'):
            current_subj = line[1:].strip()

            seq = ''
        else:
            seq = seq + line.strip()

            if index == len(data) - 1 or data[index + 1].startswith('>'):
                gc = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
                
                if gc > max_gc:
                    max_gc = gc
                    max_subj = current_subj
            
    return max_subj, max_gc

if __name__ == "__main__":
    path = 'data/rosalind_gc.txt'

    with open(path, 'r') as f:
        data = f.readlines()

    print(compute_gc(data))