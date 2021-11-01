from random import shuffle

def csv_to_list(file):
    with open(file) as f:
        L = f.read().splitlines()
    L = L[1:]
    for i, e in enumerate(L):
        L[i] = e.split(';')
    return L

def make_pairs(L):
    shuffle(L)
    length = len(L)
    M = [('', '')]*length
    for i, e in enumerate(L):
        M[i] = (L[i], L[(i+1)%length])
    return M

print(make_pairs(csv_to_list('data.csv')))
