from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t:", self.design,
              "\nRacun \t\t\t: ", self.racun,)
        
print("\n--- Ular Anaconda")      
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", " Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

print("\n--- Ular Sanca")  
sanca = Ular("Sanca", "Mamalia Kecil", "HUtan", "Bertelur", " Batik", "Tidak Berbisa")
sanca.cetak_ular()

print("\n--- Ular Mamba")  
mamba = Ular("Mamba", "Mamalia Kecil", "Perbukitan Berbatu", "Bertelur", " Hitam/Hijau ", "Berbisa")
mamba.cetak_ular()

