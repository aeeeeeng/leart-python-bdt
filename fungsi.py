def cetak(param1):
    print(param1)
    return

cetak('hello')
cetak('world')

def kuadrat(nilai):
    "kuadratkan nilai"
    return nilai*nilai
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))

def ubahParameter(listSaya):
    "tambahkan listSaya"
    listSaya = [1, 2 ,3, 4]
    print('Nilai dalam fungsi: {}'.format(listSaya))
listSaya = [10, 20, 30]
ubahParameter(listSaya)
print('Nilai diluar fungsi: {}'.format(listSaya))