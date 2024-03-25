from constants import TRANSITIONS

def transitions_and_transversions(s1: str, s2: str):
    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        if TRANSITIONS[s1[i]] == s2[i]:
            transitions += 1
        elif s1[i] != s2[i]:
            transversions += 1
    
    return transitions / transversions


if __name__ == '__main__':
    path = 'data/rosalind_tran.txt'

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

    print(transitions_and_transversions(first, second))