# scrumbling-sequences

L, S = [1,2,3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1] #Move front item to the end
    print(S, end=' ')

for i in range(len(L)):
    L = L[1:] + L[:1] #Move front item to the end
    print(L, end=' ')

for i in range(len(S)):
    X = S[i:] + S[:i] #Rear part + front part
    print(X, end=' ')

def scramble_old(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq [:1]
        yield seq

def scramble2(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in seq:
                res.append(x)
    return res

def tester(func, items, trace = True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))



def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                res.append(seq[i:i+1] +x)
        return res

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] +x

