def counting_point_mutations(s1: str, s2: str):
    mutations = 0
    for i in range(len(s1.strip())):
        if s1[i] != s2[i]:
            mutations += 1
    
    return mutations

if __name__ == "__main__":
    path ='data/rosalind_hamm.txt'

    with open(path, 'r') as f:
        seq1 = f.readline()
        seq2 = f.readline()

    print(counting_point_mutations(seq1, seq2))