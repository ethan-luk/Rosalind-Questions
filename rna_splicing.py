from typing import List
from dna_to_rna import dna_to_rna
from translate_rna_to_protein import translate_rna_to_prot

def splice_rna(main: str, intron_list: List[str]):
    for intron in intron_list:
        if intron in main:
            main = main.replace(intron, '')

    return translate_rna_to_prot(dna_to_rna(main))




if __name__ == '__main__':
    path = 'data/rosalind_splc.txt'

    with open(path, 'r') as f:
        data = f.readlines()
    
    current_seq = ''
    main_seq = ''
    is_main_seq = True
    introns = []
    count = 0
    for index, line in enumerate(data):
        if line.startswith('>'): 
            count += 1
            if count > 2:
                introns.append(current_seq)
            else:
                main_seq = current_seq
            current_seq = ''
        else:
            current_seq = current_seq + line.strip()
        
        if index == len(data) - 1:
            introns.append(current_seq)

    print(splice_rna(main_seq, introns))