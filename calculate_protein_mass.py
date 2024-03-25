from constants import PROTEIN_WEIGHTS

def calculate_prot_mass(seq: str):

    total_weight = 0
    for nuc in seq.strip():
        total_weight += PROTEIN_WEIGHTS[nuc]
    
    return total_weight

if __name__ == '__main__':
    path ='data/rosalind_prtm.txt'

    with open(path, 'r') as f:
        data = f.read()

    print(calculate_prot_mass(data))
