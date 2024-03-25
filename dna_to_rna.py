def dna_to_rna(seq: str):
    return seq.replace('T', 'U')

if __name__ == "__main__":
    path = 'data/rosalind_rna.txt'

    with open(path, 'r') as f:
        seq = f.read()
    
    print(dna_to_rna(seq))