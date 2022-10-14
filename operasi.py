contoh_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(contoh_list)
print(len(contoh_list))
print(min(contoh_list))
print(max(contoh_list))

contoh_set = [1, 2, 3, 34, 4, 5, 6, 7, 8, 9]
print(contoh_set)
print(len(contoh_set))
print(min(contoh_set))
print(max(contoh_set))

contoh_string = "aku adalah programmer python"
print(contoh_string)
print(len(contoh_string))
print(min(contoh_string))
print(max(contoh_string))

# penggabungan + replikasi (concate)
angka = [1, 2, 3, 4, 5]
huruf = ["P", "Y", "T", "H", "O", "N"]
gabung = angka + huruf
print(gabung * 2)

# range
ini_range = range(1, 100)
for i in ini_range:
    print(i)

print([_ for _ in range(0, 20, 5)])

append = []
for i in ini_range:
    append.append(i)
print(append)

kalimat = "Belajar python di dicoding sangat menyenangkan"
print("dic" in kalimat)

dataList = ["shirt", "white", "L"]
dataTuple = ["shirt", "white", "L"]
apparel, color, size = dataList
apparel, color, size = dataTuple
print(dataTuple)
