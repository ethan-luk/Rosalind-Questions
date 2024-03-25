from constants import CODON_TABLE
from dna_to_rna import dna_to_rna
from dna_complement import dna_complement

def open_reading_frames(seq: str):

    def translate_prot(rna_seq: str):
        prot_string = ''
        r = 0
        while r < len(rna_seq):
            try:
                codon = CODON_TABLE[rna_seq[r:r+3]]
            except:
                codon = ''
            
            if codon == 'Stop':
                return prot_string
            else:
                prot_string = prot_string + codon
            r += 3

    res = []

    for i in range(len(seq) - 2):
        try:
            codon = CODON_TABLE[seq[i:i+3]]
        except:
            codon = ''
        
        if codon == 'M':
            translated = translate_prot(seq[i:])
            if translated is not None:
                res.append(translated)

    return res

if __name__ == "__main__":
    path = 'data/rosalind_orf.txt'

    with open(path, 'r') as f:
        data = f.readlines()
    
    seq = ''
    for line in data:
        if not line.startswith('>'):
            seq = seq + line.strip()

    rna_seq = dna_to_rna(seq)
    reverse_complement = dna_to_rna(dna_complement(seq))

    forward = open_reading_frames(rna_seq)
    backward = open_reading_frames(reverse_complement)
    print(' '.join(set(forward + backward)))