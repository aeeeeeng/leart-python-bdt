from operator import *

hijau = 5
kuning = 10
print("Kelereng Hijau {}".format(hijau))
print("kelereng kuning {}".format(kuning))

for func in (lt, le, eq, ne, ge, gt):
    print("{}(hijau, kuning): {}".format(func.__name__, func(hijau, kuning)))
