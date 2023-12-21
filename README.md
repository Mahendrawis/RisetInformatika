# RisetInformatika
Deteksi ikan dengan metode BLOB</br>
metode  : Method

<H1> TUGAS CARI JURNAL TERBARU </H1>
Link Methodology : https://www.sciencedirect.com/science/article/pii/S0010482523008727?via%3Dihub </br>
Link Method  : https://www.sciencedirect.com/science/article/pii/S2589721723000284

<h1>HASIL & PEMBAHASAN</h1>
<h2>Pre Processing</h2>
Dalam konteks pendeteksian objek, diperlukan rangkaian prosedur terstruktur yang melibatkan pre-processing, ekstraksi fitur, dan evaluasi kesamaan hasil guna memulai proses identifikasi objek secara efektif. Citra asli yang bersifat RGB akan mengalami proses cropping dengan tujuan mendekatkan objek dan meningkatkan fokusnya. Oleh karena itu, perbandingan antara citra asli dan citra hasil cropping menghasilkan representasi visual dari objek yang berhasil diidentifikasi, menyoroti perbedaan tampilan asli dan detail objek yang diperoleh melalui proses pengolahan tersebut.
![image](https://github.com/Mahendrawis/RisetInformatika/assets/90669261/c8accf90-c71f-47f4-80e9-130d8bea0eb3)

<h2>Segmentasi Citra</h2>
Proses segmentasi citra melibatkan pemisahan atau pembagian suatu citra menjadi beberapa wilayah dengan atribut serupa, metode segmentasi berbeda-beda tergantung pada  aplikasi dan karakteristik gambar yang ada. Beberapa teknik segmentasi antara lain penggunaan algoritma seperti teknik clustering, pemrosesan tepi (edge deteksi), pemisahan warna, dan pendekatan berdasarkan pemodelan statistik. Dengan membagi gambar menjadi bagian-bagian yang lebih fokus, analisis lebih lanjut dan ekstraksi informasi dapat dilakukan dengan lebih efektif untuk mendukung berbagai  tugas dan aplikasi. Teknik segmentasi gambar, seperti yang digunakan pada Gambar 3, mengubah gambar asli menjadi gambar skala abu-abu atau biner untuk membedakan objek dari latar belakang dengan jelas dan meningkatkan kualitas analisis.

<h2>NOISE</h2>
faktor-faktor seperti interferensi elektronik, sensor, dan kondisi lingkungan selama pengambilan gambar, berbagai jenis noise dapat dihasilkan, termasuk noise Gaussian yang terdistribusi secara normal, noise salt-and-pepper yang menambahkan piksel putih atau hitam secara acak, dan noise speckle yang dihasilkan secara acak. Jika pada suatu pengambilan citra ikan hias terdapat terlalu banyak noise sehingga sulit dikenali sebagai ikan hias, faktor tersebut disebabkan karena wadah yang digunakan tidak bersih atau dengan kata lain masih terdapat warna lain selain warna putih dan pada saat pengambilan citra banyak ikan hias yang tumpang tindih.

<h2>OPERASI MORFOLOGI</h2>
Dalam konteks gambar digital, operasi morfologi mengacu pada rangkaian teknik matematika yang digunakan untuk mengubah struktur serta bentuk objek yang terdapat dalam gambar. Dua operasi dasar dalam morfologi adalah dilasi, yang meningkatkan area objek dengan menambahkan piksel yang sesuai dengan elemen struktural, dan erosi, yang mengurangi area objek dengan menghapus piksel yang sesuai dengan elemen struktural. Sebagai contoh, operasi morfologi dilasi dan erosi untuk gambar berdimensi 10x10 dan elemen struktural berdimensi 3x3.

<h1>SIMULATION PROJECT</h1>
[<img src="https://drive.google.com/file/d/1WkRA6NHUd9GJBGjwsjfmcUtSnM_ogDNj/view?usp=sharing" width="50%">](https://drive.google.com/file/d/1WkRA6NHUd9GJBGjwsjfmcUtSnM_ogDNj/view?usp=sharing "Simulasi Project")

<h2>BLOB</h2>
 Tahap segmentasi gambar memiliki dua sub-proses penting blob detection dan operasi morfologi, yang bekerja sama untuk menghasilkan hasil akhir yang dapat diinterpretasikan. Metode blob detection memainkan peran penting sebagai penunjuk strategis untuk menandai lokasi objek yang relevan. Setelah titik-titik ini diidentifikasi, diperoleh data tentang jumlah objek, tetapi perlu diingat bahwa keakuratannya tidak sepenuhnya pasti. Hal ini karena ikan hias bisa saja saling menempel atau tumpang tindih, yang dapat mempengaruhi hasil penghitungan yang sebenarnya. Seluruh proses ini dilakukan dengan menggunakan bahasa pemrograman Python selama pengujian deteksi objek untuk secara hati-hati mengevaluasi kinerja dan keakuratan hasil segmentasi untuk memastikan keakuratan dalam mengidentifikasi dan menghitung objek dalam gambar.
![image](https://github.com/Mahendrawis/RisetInformatika/assets/90669261/6cff5792-6e0f-48a1-909a-c5a18315c4ae)

<h1>HASIL</h1>
<table>
  <tr>
    <th>No</th>
    <th>Nama</th>
    <th>Hasil Uji Coba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Citra asli atau RGB</td>
    <td>87 Ikan hias</td>
  </tr>
   <tr>
    <td>2</td>
    <td>Citra biner</td>
    <td>69 Ikan hias</td>
  </tr>
   <tr>
    <td>3</td>
    <td>Citra biner tanpa noise</td>
    <td>65 Ikan hias</td>
  </tr>
   <tr>
    <td>4</td>
    <td>Morfologi citra</td>
    <td>55 Ikan hias</td>
  </tr>
   <tr>
    <td>5</td>
    <td>Blob detection</td>
    <td>51 Ikan hias</td>
  </tr>
</table>

<h1>KSEIMPULAN</h1>
Dari proses perancangan, implementasi, dan pengujian dapat diambil beberapa kesimpulan sebagai berikut :
<ul>Menerapkan metode Binary Large Object (BLOB) untuk menghitung ikan hias yang sedang berkembang biak dengan menggunakan bahasa pemrograman Python memberikan solusi yang efektif. Metode ini memungkinkan untuk menghitung ikan akuarium dalam jumlah besar dengan lebih efisien dibandingkan dengan metode manual yang menempatkan setiap ikan dalam wadah.</ul>
<ul>Metode BLOB juga telah berhasil diterapkan pada penghitungan anak burung puyuh, yang menunjukkan bahwa metode ini dapat meningkatkan kecepatan penghitungan dan mengurangi kemungkinan kesalahan. Hal ini memudahkan peternak puyuh untuk menghitung jumlah anakan puyuh secara lebih efisien.</ul>
<ul>Perancangan pengolahan citra digital menggunakan metode BLOB dengan bahasa pemrograman Python menggunakan langkah yang terstruktur. Sebelum dilakukan komputasi menggunakan metode BLOB, citra RGB diubah menjadi citra grayscale dan biner. Kemudian, operasi morfologi seperti dilasi dan erosi diterapkan untuk menghilangkan noise citra dan memisahkan ikan hias yang saling berdekatan atau tumpang tindih.</ul>
<ul>Tingkat akurasi citra uji objek dalam grayscale mencapai 75 dengan 20 data uji. Dari jumlah tersebut, 15 titik data memberikan hasil yang benar dan 5 titik data memberikan hasil yang salah. Kesalahan pengujian disebabkan oleh kombinasi warna latar belakang yang berbeda atau kondisi gambar yang terlalu gelap, sehingga aplikasi cenderung menganggap objek sebagai bagian dari latar belakang. Evaluasi ini memberikan wawasan penting tentang faktor-faktor yang dapat mempengaruhi akurasi proses pengujian.</ul>

<h1>HAK CIPTA</h1>
JURNAL INI MILIK MAHENDRA WISNU WARDANA, IMAM MASKURI, SYARIFUZ ZAIM.
TERBIT JURNAL INI KARENA TUGAS PCD & DILANJUTKAN DI RISET





