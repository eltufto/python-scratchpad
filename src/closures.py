flist = []

for i in xrange(3):
    def funcC(j):
        def func(x): return x * j
        return func
    flist.append(funcC(i))

for f in flist:
    print f(2)
