------------------Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> NAMA = 'Yudha Gana P.W'
>>> NIM = 'L200180150'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(NAMA)
>>> type(a)
<type 'int'>
>>> type(b)
<type 'int'>
>>> a / b
82
>>> #python membagi a dan b
>>> a // b
82
>>> #python membagi dengan pembulatan kebawah
>>> 10 * (a - 999)
1510
>>> #python mengambil angka di a lalu dikurangi 999 dan hasilnya dikalikan 10
>>> b ** 2
196
>>> #python mengambil angka di b lalu dipangkatkan 2
>>> a % b
2
>>> #2 merupakan sisa hasil bagi dari angka a dan angka b
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> a / c
92.0
>>> #python mengambil angka a lalu dibagi dengan angka c
>>> a // c
92.0
>>> #92 merupakan sisa hasil bagi dari angka a dan c yang merupakan bentuk desimal karena angka c merupakan float
>>> #pernyataan diatas salah karena angka 92 merupakan pembagian dengan pembulatan kebawah dari angka a dan c
>>> a % c
0.0
>>> #0.0 merupakan sisa hasil bagi dari bilangan a dan c
>>> c > b
False
>>> #salah karena angka c lebih kecil dari angka b
>>> type(c > b)
<type 'bool'>
>>> a > b and b > c
True
>>> #benar karena angka a lebih besar dari angka b dan angka b lebih besar dari angka c
>>> a > 1100 or b < 10
True
>>> #benar karena angka a lebih besar dari 1100 atau angka b  lebih kecil dari angka 10
>>> 
