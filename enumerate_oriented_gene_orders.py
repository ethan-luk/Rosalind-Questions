from itertools import permutations

def enumerate_oriented_gene_orders(num):
    perms = list(permutations(range(1,num + 1)))

    print(len(perms))

    for perm in perms:
        print(' '.join(map(str, perm)))
    
    return len(perms), perms



if __name__ == '__main__':
    enumerate_oriented_gene_orders(5)
