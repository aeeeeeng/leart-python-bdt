class Kalkulator:
    """contoh kelas kalkulator sederhana"""
    i = 12345

    def __init__(self, i=1234):
        self.i = i

    def f(self):
        return 'Hello World'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)
    
# Kalkulator.i = 2020
print(Kalkulator.i)

# method dari object
k = Kalkulator(i=2020)  # membuat instance dari kelas jadi objek, kemudian disimpan pada variabel k\
print(k.i)

# method class
print(Kalkulator.tambah_angka(1, 1))

# method static
print(Kalkulator.kali_angka(10, 10))

