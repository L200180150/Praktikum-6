Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Yudha Gana P.W'
>>> NIM = 150
>>> Tinggi = 1.71
>>> Berat = 86
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> Aku[0]
2001
>>> a = NIM % 4; Aku[a]
1.71
>>> #1.71 merupakan sisa hasil bagi dari angka NIM dan angka 4
>>> type(Aku[a])
<type 'float'>
>>> Aku[a:4]
(1.71, 150)
>>> #python menampilkan hasil dari program yaitu (1.71, 150)
>>> type(Aku[4])
<type 'str'>
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #eror karena objek tidak mendukung perintah tersebut
>>> type(Data)
<type 'list'>
>>> type(Data[4])
<type 'str'>
>>> Data[4][5]
' '
>>> Data[4][a:6]
'dha '
>>> #python menampilkan respond dengan kata dha yang merupakan anggota dari data
>>> Data[0] = 'ok'; Data
['ok', 86, 1.71, 150, 'Yudha Gana P.W']
>>> #python menampilkan seluruh isi data
>>> Data[-a]
150
>>> #menampilkan anggota dari data yaitu NIM 150
>>> range(a)
[0, 1]
>>> menampilkan hasil program yaitu[0, 1]
