Laporan Praktikum: Analisis Performa Penjualan E-commerce
1. Business Question
Dalam praktikum ini, analisis dilakukan untuk menjawab beberapa pertanyaan kunci:
-Bagaimana tren penjualan bulanan selama periode pengamatan?
-Apakah biaya iklan berpengaruh signifikan terhadap total penjualan?
-Siapa pelanggan terbaik kita berdasarkan metode RFM (Recency, Frequency, Monetary)?
-Wilayah mana yang memberikan profit paling rendah sehingga perlu dievaluasi?

2. Data Wrangling
Proses pembersihan data yang telah dilakukan meliputi:
Konversi Tipe Data: Mengubah kolom Order_Date menjadi format datetime agar bisa diolah secara kronologis.
Handling Missing Values: Mengisi nilai kosong pada Total_Sales dengan hasil perkalian Quantity dan Price_Per_Unit.
Filtering: Memastikan tidak ada data anomali seperti harga atau kuantitas yang bernilai negatif.
Feature Engineering: Membuat kolom baru seperti Month untuk tren bulanan dan skor RFM untuk segmentasi pelanggan.

3. Insights
Berdasarkan visualisasi yang dihasilkan, ditemukan beberapa poin penting:
Tren Penjualan: Penjualan cenderung mengalami fluktuasi, dengan puncak tertinggi terjadi pada bulan [masukkan bulan sesuai grafikmu].
Korelasi & Regresi: Biaya iklan memiliki pengaruh positif terhadap penjualan. Berdasarkan model Regresi Linear, setiap kenaikan biaya iklan diikuti oleh kenaikan penjualan dengan akurasi (R2 Score) sebesar [masukkan nilai skor kodinganmu].
Peta Korelasi: Heatmap menunjukkan hubungan yang kuat antara biaya iklan dan total penjualan dibandingkan variabel lainnya.
Produk & Stok: Melalui Scatter Plot, ditemukan beberapa produk dengan stok (Inventory) tinggi namun terjual (Quantity) rendah.

4. Recommendation
Berdasarkan temuan di atas, berikut adalah saran aksi untuk perusahaan:
Optimasi Stok: Melakukan cuci gudang atau promo khusus untuk produk yang memiliki stok menumpuk namun perputarannya lambat.
Strategi Iklan: Terus mengalokasikan anggaran pada iklan digital karena terbukti efektif meningkatkan konversi penjualan.
Loyalty Program: Memberikan apresiasi atau promo eksklusif kepada pelanggan di segmen "Best Customers" (Skor RFM 555) agar mereka tetap setia.
Evaluasi Wilayah: Melakukan evaluasi logistik atau strategi pemasaran di wilayah dengan profit margin terkecil untuk menekan biaya operasional.

hasil dari kelompokan nomor 1:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e4879877-0250-4a6f-96fc-434005266679" />

hasil dari kelompokan nomor 2 dan 5:
<img width="1484" height="382" alt="image" src="https://github.com/user-attachments/assets/56a67e4d-c76f-40fa-890e-6dd0e831f2d2" />

hasil dari kelompokan nomor 3:
<img width="1368" height="769" alt="image" src="https://github.com/user-attachments/assets/d3c06de7-b352-4b1f-a2f7-770c2cba8ea5" />

hasil dari kelompokan nomor 4:
<img width="1022" height="750" alt="image" src="https://github.com/user-attachments/assets/38e5460c-4dbd-4362-b802-b33a3b7eb8dc" />

hasil dari kelompokan nomor 6:
<img width="1484" height="134" alt="image" src="https://github.com/user-attachments/assets/d1d46e74-805a-4f4f-8c5b-2f7092d78769" />
