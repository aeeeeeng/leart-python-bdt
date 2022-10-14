for huruf in 'Dicoding':
    print('Huruf {}'.format(huruf))

flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:
    print('Bunga {}'.format(flower))

for index in range(len(flowers)):
    print('Bunga {}'.format(flowers[index]))

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()