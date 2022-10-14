# break
for huruf in 'dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini {}'.format(huruf))

for i in range(0, 10):
    for j in range(0, 10):
        if j>i:
            print()
            break
        else:
            print('*', end="\n")

# continue
for huruf in 'dico-ding':
    if huruf == '-':
        continue
    print('Huruf saat ini {}'.format(huruf))

# else setelah for
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        print(n, ' adalah bilangan prima')

for n in range(0, 10):
    if n % 2 == 0:
        print(n, 'hore')
    else:
        print(n, 'oh nooo')
    
# pass
def sebuahFungsi():
    pass

import sys
data = ''
while(data != 'exit'):
    try:
        data = input('Please enter an integer (type exit to exit):')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass
        else:
            print('error {}'.format(sys.exc_info()[0]))

# inline loop
# contoh 1
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
# contoh 1 = inline loop
pangkat = [n**2 for n in angka]
print(pangkat)

#contoh 2
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)
print(duplikat)
# contoh 2 = inline loop
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat)

# contoh 3
list_a = ['Hello', 'world', 'in', 'python']
small_list_a = []
for a in list_a:
    small_list_a.append(a.lower())
print(small_list_a)
# contoh 3 = inline loop
small_list_a = [a.lower() for a in list_a]
print(small_list_a)