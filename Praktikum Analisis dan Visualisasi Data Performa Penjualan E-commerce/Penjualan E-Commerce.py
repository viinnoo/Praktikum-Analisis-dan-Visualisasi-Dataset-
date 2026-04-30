# Langkah 1: Persiapan Library & Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

df = pd.read_csv('data_praktikum_analisis_data.csv')

# Langkah 2: Inspeksi & Pembersihan Data (Data Cleaning)
# print(df.head())
# print(df.info())
# df.isnull().sum()
# df = df[df['Price_Per_Unit'] > 0]

# Langkah 3: Analisis & Visualisasi
# - Analisis Tren Penjualan Bulanan (Line Chart)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
# df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
# monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# plt.figure(figsize=(10,5))
# plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
# plt.title('Tren Penjualan Bulanan')
# plt.xticks(rotation=45)
# plt.show()

# - Analisis Korelasi (Heatmap)
# correlation = df[['Total_Sales', 'Ad_Budget', 'Price_Per_Unit']].corr()
# sns.heatmap(correlation, annot=True, cmap='coolwarm')
# plt.title('Peta Korelasi Antar Variabel')
# plt.show()

# Langkah 4: nyari data-data yang kosong/belum ada:
# Total_Sales yang kosong (Quantity * Price):
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price_Per_Unit'])

# Data dummy buat Tugas Siswa yang ilang/belum ada:
np.random.seed(42)
df['Inventory'] = np.random.randint(50, 500, size=len(df)) # Untuk Tugas 1
df['Region'] = np.random.choice(['Jakarta', 'Bandung', 'Surabaya', 'Medan'], size=len(df)) # Untuk Tugas 3
df['Discount_Percentage'] = np.random.uniform(0, 0.4, size=len(df)) # Untuk Tugas 4
df['Profit'] = df['Total_Sales'] * np.random.uniform(0.1, 0.3, size=len(df)) # Untuk Tugas 3

# Tugas Siswa:
# 1. Identifikasi Produk:
# plt.figure(figsize=(10,6))
# sns.scatterplot(data=df, x='Inventory', y='Quantity', hue='Product_Category')
# plt.title('Analisis Stok (Inventory) vs Penjualan')
# plt.xlabel('Jumlah Stok di Gudang')
# plt.ylabel('Jumlah Produk Terjual')
# plt.grid(True)
# plt.show()

# 2. Segmentasi Pelanggan (RFM Analysis) & 5. Pendalaman Teknik: RFM Analysis:
# Tentukan tanggal snapshot (hari esok dari transaksi terakhir)
# snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

# # Hitung R, F, M
# rfm = df.groupby('CustomerID').agg({
#     'Order_Date': lambda x: (snapshot_date - x.max()).days, # Recency
#     'Order_ID': 'count',                                   # Frequency
#     'Total_Sales': 'sum'                                   # Monetary
# })

# # Rename kolom & Beri Skor 1-5 [cite: 279, 281]
# rfm.columns = ['Recency', 'Frequency', 'Monetary']
# rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
# rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
# rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# # Gabungkan skor untuk segmen [cite: 284]
# rfm['RFM_Group'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)
# print(rfm.head())

# 3. Analisis Kontribusi Kategori:
# geo_profit = df.groupby('Region')['Profit'].sum().sort_values()

# plt.figure(figsize=(10,5))
# geo_profit.plot(kind='barh', color='skyblue')
# plt.title('Total Profit per Wilayah (Urut Terendah ke Tertinggi)')
# plt.xlabel('Total Keuntungan')
# plt.show()

# 4. Uji Hipotesis Sederhana:
# df['Promo_Kategori'] = df['Discount_Percentage'] > 0.20
# analisis_diskon = df.groupby('Promo_Kategori')['Quantity'].mean()

# plt.figure(figsize=(8,5))
# analisis_diskon.plot(kind='bar', color=['grey', 'orange'])
# plt.title('Rata-rata Penjualan: Diskon > 20% vs Rendah')
# plt.xticks([0, 1], ['Diskon Low', 'Diskon High (>20%)'], rotation=0)
# plt.ylabel('Rata-rata Produk Terjual')
# plt.show()

# # 6. Regresi Linear Sederhana:
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # Pastikan kolom sudah bersih dari nilai NaN agar tidak error lagi
# df_clean = df.dropna(subset=['Ad_Budget', 'Total_Sales'])

# X = df_clean[['Ad_Budget']] 
# y = df_clean['Total_Sales']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# print(f"Koefisien Iklan: {model.coef_[0]}")
# print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test)}")