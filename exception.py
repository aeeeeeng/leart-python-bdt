z = 0
try:
    print(1/z)
except ZeroDivisionError:
    print('Tidak bisa membagi dengan 0')

try:
    with open('testa.py') as file:
        print(file.read())
except (FileNotFoundError, ZeroDivisionError):
    print('File tidak ditemukan')

d = {'ratarata': '10.9'}
try:
    print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:
    print('kunci tidak ditemukan')
except (ValueError, TypeError,):
    print('nilai tidak sesuai')

if 'total' not in d:
    raise KeyError('Harus memiliki key total')