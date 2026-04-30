print("hallo")

#soal 1
#data int
a=3
print(type(a))

#data float
b=3.5 
print(type(b))

#data list
angka=[1,2,3,4,5]
print(type(angka)) 
print(angka)
angka.append(6)
print(angka)

#soal 2
belanja=["beras", "minyak", "telur"]
print(type(belanja))
belanja.append("gula")
belanja.append("kopi")
print(belanja)

#soal 3
daftarHarga = {
    "beras":12000, 
    "minyak":17000, 
    "telur":24000, 
    "gula":15000, 
    "kopi":20000
}
belanjaan = ['beras', 'telur', 'gula', 'kopi', 'minyak']

listHarga = [daftarHarga[x] for x in belanjaan]
print(listHarga)
 
totalHarga = sum(listHarga)
print(totalHarga)

#soal 4
def luas_Keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    print("Luas Persegi Panjang:", luas)
    print("Keliling Persegi Panjang:", keliling)
    return luas, keliling
print(luas_Keliling(5, 10))

#soal 5
def cekUmur(umur):
    if umur < 14:
        return "Anda masih anak-anak"
    elif umur >= 14 and umur <25: 
        return "Anda sudah remaja"
    elif umur >= 25 and umur < 50:
        return "Anda masih dewasa"
    elif umur >= 50:
        return "Anda sudah tua"
    
input_umur = int(input("Masukkan umur Anda: "))
print(cekUmur(input_umur))