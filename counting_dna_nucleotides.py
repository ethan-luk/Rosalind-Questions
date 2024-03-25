def counting_dna_nucleotides(seq: str):
    d = {}

    for nuc in seq.strip():
        d[nuc] = d.get(nuc, 0) + 1

    return d


if __name__ == "__main__":
    path = 'data/rosalind_dna.txt'

    with open(path, "r") as f:
        seq = f.read()
    
    print(counting_dna_nucleotides(seq))