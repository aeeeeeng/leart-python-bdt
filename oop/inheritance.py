class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""
    def __init__(self, nilai=0):
        self.nilai = nilai
    
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9: # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai

class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas sederhana"""
    def kali_angka(self, angka1, angka2):
        self.nilai = angka1+angka2
        return self.nilai
    
    # overide
    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:
            super().tambah_angka(angka1, angka2)
        else:
            self.nilai = angka1 + angka2
        return self.nilai

kk = KalkulatorKali()
a = kk.kali_angka(2, 3)
print(a)

b = kk.tambah_angka(5, 6)
print(b)


# attribute dinamis
class Pegawai:
    pass

emp = Pegawai()
emp.nama = 'Syahril'
emp.bagian = 'IT'
emp.gaji = '20,000,000'
print(emp.nama)