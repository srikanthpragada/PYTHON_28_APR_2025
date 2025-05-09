l1 = [10, 20, 30, 40]
l2 = ['abc', 'xyz', 'pqr']

for fv, sv in zip(l1, l2, strict = True):
    print(fv, sv)