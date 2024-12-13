from Animal import *

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, bulu ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.bulu = bulu

    def cetak_kucing(self):
        super().cetak()
        print("Warna \t\t\t:", self.warna,
              "\nBulu \t\t\t: ", self.bulu,)
        
print("\n--- Kucing Anggora")         
anggora = Kucing("Anggora", "Daging", "Darat", "Beranak", " Putih", "Tebal")
anggora.cetak_kucing()

print("\n--- Kucing Persia") 
persia = Kucing("Persia", "Ikan", "Darat", "Beranak", " Oranye", "Tebal")
persia.cetak_kucing()

print("\n--- Kucing Ragdoll") 
ragdoll = Kucing("Ragdoll", "Daging", "Darat", "Beranak", " Putih", "Tebal")
ragdoll.cetak_kucing()