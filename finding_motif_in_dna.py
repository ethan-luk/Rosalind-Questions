def finding_motif_in_dna(s: str, t: str):
    l = 0
    res = []
    for r in range(len(t), len(s)):
        if s[l:r] == t:
            res.append(l + 1)
        l += 1

    return res

if __name__ == "__main__":
    path = 'data/rosalind_subs.txt'

    with open(path, 'r') as f:
        seq = f.readline().strip()
        subseq = f.readline().strip()

    print(finding_motif_in_dna(seq, subseq))