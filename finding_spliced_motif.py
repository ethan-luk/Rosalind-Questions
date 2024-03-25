def find_spliced_motif(s1, s2):
    p2 = 0
    res = []
    for i in range(len(s1)):
        if s1[i] == s2[p2]:
            res.append(i + 1)
            p2 += 1
            if p2 == len(s2):
                break
    return res

    

if __name__ == '__main__':
    path = 'data/rosalind_sseq.txt'

    with open(path, 'r') as f:
        data = f.readlines()

    current_seq = ''
    for index, line in enumerate(data):
        if not line.startswith('>'):
            current_seq = current_seq + line.strip()
        elif index != 0:
            first = current_seq
            current_seq = ''

    second = current_seq

    print(find_spliced_motif(first, second))