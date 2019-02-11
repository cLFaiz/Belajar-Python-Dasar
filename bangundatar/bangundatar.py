# Menghitung Luas Bangun Datar#

def luas_pesegi(sisi):
    print("Luas Persegi")
    luas = (sisi * sisi)
    print("Hasilnya adalah : ", luas)
    tanya()


#segitiga
def luas_segitiga(alas, tinggi):
    print("Luas Segitiga")
    luas = 0.5 * (alas * tinggi)
    print("Hasilnya adlah : ", luas)
    tanya()

#Lingkaranx

#pilihan
def menu():
    pil = int(input("Pilihannya rumus : \n\t 1. Persegi \n\t 2. Segitiga \n\t 3. Lingkaran \n\t 4. Jajar Genjang \nSilahkan pilih : "))
    if pil == 1:
        luas_pesegi(sisi=int(input("Masukan sisi : ")))
    elif pil == 2:
        luas_segitiga(alas=float(input("Masukan alas : ")), tinggi=float(input("Masukan tinggi : ")))
    else:
        print("Salah memasukan pilihan")
    tanya()

def tanya():
    tanya = input("Ingin lagi ? y/t ")
    if tanya == 'y':
        menu()
    elif tanya =='t':
        exit()
    else:
        "salah input :v"

#         start! :'v
username = input("Masukan Username : ")
password = input("Masukan Password : ")
if username == "faiz" and password == "123":
    menu()
else:
    print("Username atau password salah")