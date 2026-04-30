#Import Library 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#Langkah 2 – Import Data dari File CSV 
df = pd.read_csv("Data_Penjualan_Toko_Online.csv") 
print (df.head())

#Mengecek dan Membersihkan Data 
print (df.info())
print (df.isnull().sum())
# Jika ada nilai kosong
df = df.dropna()

# Analisis Deskriptif 
print ("Statistik Deskriptif:")
print (df.describe())

print ("\nProduk Terlaris:")
print (df.groupby('Produk')['Jumlah'].sum().sort_values(ascending=False))

#Visualisasi Data 
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Produk', y='Pendapatan', estimator=sum, ci=None)
plt.title("Total Pendapatan per Produk")
plt.show()


plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='Tanggal', y='Pendapatan', markers="o")
plt.title("Tren Pendapatan Mingguan")
plt.show()

df["Diskon"] = 0.10
df["Pendapatan_Bersih"] = df["Pendapatan"] - (df["Pendapatan"] * df["Diskon"])

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Produk", y="Pendapatan_Bersih", estimator=sum, ci=None)
plt.title("Total Perndapatan Bersih per Produk")
plt.ylabel("Pendapatan Bersih (Rp)")
plt.xlabel("Produk")
plt.show()

#Menyimpan Hasil Analisis 
df.to_csv("hasil_analisis_penjualan.csv", index=False) 
print("Data hasil analisis telah disimpan sebagai hasil_analisis_penjualan.csv")