from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t:", self.jenis,
              "\nBunyi \t\t\t: ", self.bunyi,)
        
print("\n--- Ular Mamba")  
kenari_atlantik = Burung("Kenari Atlantik", "Biji", "Udara", "Bertelur", " Pipit", "Menciap")
kenari_atlantik.cetak_burung()

print("\n--- Burung Cenderawasi Biru") 
cenderawasih = Burung("Cenderawasih biru", "Serangga", "Udara", "Bertelur", " Cenderawasih", "Mencicit")
cenderawasih.cetak_burung()

print("\n--- Burung Love Bird") 
love_Bird = Burung("Love Bird", "Sayuran", "Udara", "Bertelur", " Misty", "Menciap")
love_Bird.cetak_burung()

