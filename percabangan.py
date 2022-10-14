# cek bilangan ganjil menggunakan modulus
bilangan = 4
if bilangan % 2 == 0:
    print("Bilangan {} adalah genap".format(bilangan))
else:
    print("Bilangan {} adalah ganjil".format(bilangan))

#percabangan else if
nilai_siswa = int(input('masukkan nilai tugas:'))
if nilai_siswa > 80:
    print("A")
elif nilai_siswa > 70:
    print("B")
elif nilai_siswa > 60:
    print("C")
else:
    print("D")