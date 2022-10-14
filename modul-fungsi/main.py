import sys
sys.path.append('D:\\learn-python\\dicoding-bdt\\modul-fungsi\\modul')
import hello

hello.world()

print(hello.nama)

syahril = hello.Reviewer(hello.nama, "Python")
syahril.review()