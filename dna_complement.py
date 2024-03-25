from constants import COMPLEMENTS

def dna_complement(seq: str):
    complement = ''

    for nuc in seq.strip():
        complement = complement + COMPLEMENTS[nuc]
    
    return complement[::-1]

if __name__ == "__main__":

    path = 'data/rosalind_revc.txt'

    with open(path, 'r') as f:
        seq = f.read()
    
    print(dna_complement(seq))