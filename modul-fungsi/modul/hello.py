def world():
    print("Hello World")

nama = 'Syahril Ardi'

class Reviewer:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab atas kelas " + self.kelas)