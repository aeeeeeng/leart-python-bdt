#NUMBER
a = 10
print(a, "bertipe", type(a))
b = 1.7
print(b, "bertipe", type(b))
c = 1+2j
print(c, "bertipe", type(c))

x=[0]*10005
x[1] = 1

for j in range(2, 10001):
    x[j]=x[j-1]+x[j-2]
print(x[10000])

#STRING
tunggal="Ini adalah string tunggal"
multi='''ini adalah String
yang memiliki baris pertama
dan selanjutnya baris kedua
'''
print(tunggal)
print(multi)

#LIST
a = [1, 2.2, 'bayu']
print(a[:-1])

list = [5,10,15,20,25,30,35,40]
print(list[5])
print(list[-1])
print(list[0:5])
print(list[:5])
print(list[-3:])
print(list[1:7:2])

list.append(45)
del list[8]
print(list)

#SLICING PADA STRING
string = "Hello World"
# print(string(3))

# TUPLE
tuple = (5, 'Bayu', 1+3j)
print(tuple[1])
print(tuple[0:3])
# print(tuple[0]=1)

# SET
set = {1,2,2,3,3,3}
print(set)

# DICTIONARY
dictionary = {1: 'value', 'key': 2}
print('dictionary[1]:', dictionary[1])
print('dictionary[key]:', dictionary['key'])
print(type(dictionary[1]))