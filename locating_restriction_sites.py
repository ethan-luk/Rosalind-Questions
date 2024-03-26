from dna_complement import dna_complement

def locate_restriction_sites(seq):
    res = []
    for i in range(len(seq) - 3):
        for length in range(4, 13):
            if i + length > len(seq):
                break
            if seq[i:i+length] == dna_complement(seq[i:i+length]):
                res.append((i + 1, length))
    return res

if __name__ == '__main__':
    path = 'data/rosalind_revp.txt'

    with open(path, 'r') as f:
        data = f.readlines()
    
    seq = ''
    for line in data:
        if not line.startswith('>'):
            seq = seq + line.strip()

    print(locate_restriction_sites(seq))