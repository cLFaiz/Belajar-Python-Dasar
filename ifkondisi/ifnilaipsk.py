p = int(input("Nilai Pengetahuan : "))
s = int(input("Nilai Sikap : "))
k = int(input("Nilai Keterampilan : "))

if (p >= 75) & (s >= 75) & (k >= 75):
    print("Selamat Kamu Kompeten")
elif (p < 75 ) & (s >= 75) & (k >= 75):
    print("Nilai Pengetahuan Kamu Belum Kompeten")
elif (p >= 75) & (s < 75 ) & (k >= 75):
    print("Nilai Sikap kamu belum kompeten")
elif (p >= 75) & (s >=75 ) & (k < 75 ):
    print("Nilai Keterampilan kamu belum kompeten")
elif (p <75 ) & (s <75 ) & (k >= 75):
    print("Nilai Pengetahun dan Sikap kamu belum kompeten")
elif (p >= 75) & (s <75 ) & (k <75):
    print("Nilai sikap dan keterampilan kamu belum kompeten")
elif (p <75 ) & (s >= 75) & (k <75):
    print("Nilai Pengetahuna dan Keterampilan kamu belum kompeten")
elif (p <75) & (s <75 ) & (k <75 ):
    print("belum kompeten dari segala aspek !!!")