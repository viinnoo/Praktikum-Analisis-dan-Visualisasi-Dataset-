import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Kucing:
 # Constructor
    def __init__(self, nama, warna):
        self.nama = nama # Attributeself.warna = warna # Attribute
        self.warna = warna # Attribute
 # Method
    def suara(self):
        return f"{self.nama} berkata: Meow!"
# Membuat Object (Instansiasi)
kucing1 = Kucing("Luna", "Putih")
kucing2 = Kucing("Garfield", "Oranye")
# Mengakses Attribute dan Method
print(kucing1.nama) # Output: Luna
print(kucing2.suara()) # Output: Garfield berkata: Meow!