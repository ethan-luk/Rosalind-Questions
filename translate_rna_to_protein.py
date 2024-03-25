from constants import CODON_TABLE

def translate_rna_to_prot(seq):
    r = 0
    prot_string = ''
    while r < len(seq.strip()) - 1:
        if CODON_TABLE[seq[r:r+3]] != 'Stop':
            prot_string = prot_string + CODON_TABLE[seq[r:r+3]]
        r += 3
    return prot_string

if __name__ == "__main__":
    path = 'data/rosalind_prot.txt'

    with open(path, 'r') as f:
        data = f.read()
    
    print(translate_rna_to_prot(data))