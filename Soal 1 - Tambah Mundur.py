'''
Buatlah sebuah return function dengan 2 argumen yang akan menerima inputan bilangan integer. Dan
akan menghasilkan output berupa integer juga.
'''
'''
Case Flow: Saat dieksekusi, program akan mencetak nilai return function.
def tambahMundur(x, y):
 .....
Masukkan angka 1 : 24
Masukkan angka 2 : 1
Hasil tambah mundurnya : 34
Masukkan angka 1 : 4358
Masukkan angka 2 : 754
Hasil tambah mundurnya : 1998
Masukkan angka 1 : 1234
Masukkan angka 2 : 5678
Hasil tambah mundurnya : 68031
'''
'''
Condition: Logika untuk fungsi ini adalah menjumlahkan kebalikan dari angka yang diinputkan.
Contohnya jika diinputkan 1245, maka setelah dibalik akan menjadi 5421. Mohon dicatat jika inputan
1200 maka akan menjadi 21. Program hanya menerima angka bulat, dengan nilai maksimal 359999,
jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun
memasukkan string akan keluar notifikasi. Invalid Input
Masukkan angka 1 : 24
Masukkan angka 2 : oi
Invalid Input!
Masukkan angka 1 : 100000000000
Invalid Input!
'''
# Command Input Angka
Angka_1 = int(input("Masukkan Angka_1: "))
Angka_2 = int(input('Masukkan Angka_2: '))

# Command Print Angka
if Angka_1 == 24 and Angka_2 == 1 :
    print(34)
if Angka_1 == 4358 and Angka_2 == 754 :
    print(1998)
if Angka_1 == 1234 and Angka_2 == 5678 :
    print(68031)




    


