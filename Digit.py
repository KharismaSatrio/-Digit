#Soal_3
def digitAwal(a,b): #fungsi digunakan untuk mengambil nilai paling awal
    c=a**b #operasi matematika a pangkat b yang di masukan ke variabel c
    cc = (str(c))[0] #disini variabel c dijadikan string, dan digunakan fungsi slice untuk mengambil variabel paling awal dan di assign ke variabel baru
    return cc #kemudian cc dari perhitungan line ke 4 di return

def digitAkhir(a,b):#fungsi digunakan untuk mengambil nilai paling akhir
    c=a**b #operasi matematika a pangkat b
    cc = (str(c))[-1] #disini variabel c dijadikan string, dan digunakan fungsi slice untuk mengambil variabel paling akhir dan di assign ke variabel baru
    return cc #kemudian cc dari perhitungan line ke 4 di return

print(digitAwal(10,8)) # mencetak hasil dari fungsi digit awal dengan 2 argumen
print(digitAwal(2,3))
print(digitAwal(6,3))

print(digitAkhir(10,8)) # mencetak hasil dari fungsi digit akhir dengan 2 argumen
print(digitAkhir(2,3))
print(digitAkhir(6,3))


