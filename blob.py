import cv2
import matplotlib.pyplot as plt
from skimage.morphology import remove_small_objects
from skimage.feature import blob_log
import numpy as np
from google.colab.patches import cv2_imshow

# Baca gambar dari file
gambar = cv2.imread('ikan.jpg')

# Reduksi ukuran gambar menjadi 16:9
tinggi, lebar, _ = gambar.shape
rasio_tinggi = 9
rasio_lebar = 16
lebar_baru = int(tinggi * (rasio_lebar / rasio_tinggi))
gambar_reduksi = cv2.resize(gambar, (lebar_baru, tinggi))

# Simpan gambar hasil reduksi (opsional)
cv2.imwrite('ikan_reduksi.jpg', gambar_reduksi)

# Tampilkan gambar hasil reduksi menggunakan matplotlib
plt.imshow(cv2.cvtColor(gambar_reduksi, cv2.COLOR_BGR2RGB))
plt.show()

# Pilih objek ikan (tentukan koordinat sudut kiri atas dan kanan bawah untuk cropping)
x1, y1, x2, y2 = 100, 330, 340, 430

# Crop citra untuk mendapatkan objek yang lebih dekat
objek_ikan = gambar_reduksi[y1:y2, x1:x2]

# Simpan citra yang sudah di-crop (opsional)
cv2.imwrite('citra_crop.jpg', objek_ikan)
plt.imshow(cv2.cvtColor(objek_ikan, cv2.COLOR_BGR2RGB))
plt.show()

# Ubah objek ikan menjadi 10x20
objek_ikan_kecil = cv2.resize(objek_ikan, (20, 10))

# Simpan gambar hasil reduksi (opsional)
cv2.imwrite('ikan_kecil.jpg', objek_ikan_kecil)

# Tampilkan gambar objek ikan yang sudah diubah ukurannya menggunakan matplotlib
plt.imshow(cv2.cvtColor(objek_ikan_kecil, cv2.COLOR_BGR2RGB))
plt.show()

# Baca gambar reduksi
gambar_reduksi = cv2.imread('ikan_reduksi.jpg')

# Ubah gambar menjadi citra grayscale
grayscale = cv2.cvtColor(gambar_reduksi, cv2.COLOR_BGR2GRAY)
# Simpan citra grayscale (opsional)
cv2.imwrite('ikan_grayscale.jpg', grayscale)

# Tampilkan citra grayscale
plt.imshow(grayscale, cmap='gray')
plt.title('Citra Grayscale')
plt.show()

# Lakukan denoising menggunakan Non-Local Means Denoising
denoised = cv2.fastNlMeansDenoising(grayscale, None, h=10, templateWindowSize=7, searchWindowSize=21)
# Simpan citra denoised (opsional)
cv2.imwrite('ikan_denoised.jpg', denoised)

# Tampilkan citra denoised
plt.imshow(denoised, cmap='gray')
plt.title('Citra Denoised')
plt.show()

# Lakukan thresholding untuk membuat citra biner
_, biner = cv2.threshold(denoised, 125, 255, cv2.THRESH_BINARY)
# Simpan citra biner (opsional)
cv2.imwrite('ikan_biner.jpg', biner)

# Tampilkan citra biner
plt.imshow(biner, cmap='gray')
plt.title('Citra Biner')
plt.show()

# Baca gambar kecil
gambar_kecil = cv2.imread('ikan_kecil.jpg')

# 1. Tampilkan nilai matriks RGB dengan R sendiri G sendiri dan B sendiri
r, g, b = cv2.split(gambar_kecil)

print("Nilai matriks untuk saluran merah (R):")
print(r)
print("Nilai matriks untuk saluran hijau (G):")
print(g)
print("Nilai matriks untuk saluran biru (B):")
print(b)

# 2. Ubah gambar menjadi citra grayscale dan tampilkan matriks
grayscale = cv2.cvtColor(gambar_kecil, cv2.COLOR_BGR2GRAY)
# simpan citra grayscale (opsional)
cv2.imwrite('ikan_kecil_grayscale.jpg', grayscale)
print("Nilai matriks untuk citra grayscale:")
print(grayscale)

plt.imshow(grayscale, cmap='gray')
plt.title('Citra Grayscale')
plt.show()

# 3. Lakukan thresholding untuk membuat citra biner dan tampilkan matriks hanya 0 dan 1
_, biner = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY)
# Simpan citra biner (opsional)
cv2.imwrite('ikan_kecil_biner.jpg', biner)
biner = biner / 255  # Normalisasi nilai ke 0 dan 1

print("Nilai matriks untuk citra biner:")
print(biner)

plt.imshow(biner, cmap='gray')
plt.title('Citra Biner')
plt.show()

# Baca gambar biner yang telah dihilangkan noise
gambar_kecil_biner = cv2.imread('ikan_kecil_biner.jpg', cv2.IMREAD_GRAYSCALE) / 255
gambar_asli_biner = cv2.imread('ikan_biner.jpg', cv2.IMREAD_GRAYSCALE) / 255

# Hilangkan noise pada gambar kecil
gambar_kecil_tanpa_noise = remove_small_objects(gambar_kecil_biner.astype(bool), min_size=10, connectivity=2)

# Hilangkan noise pada gambar asli
gambar_asli_tanpa_noise = remove_small_objects(gambar_asli_biner.astype(bool), min_size=10, connectivity=2)

# Deteksi blob pada gambar kecil tanpa noise
blobs_kecil = blob_log(gambar_kecil_tanpa_noise, min_sigma=7, max_sigma=4, num_sigma=1, threshold=0.02)

# Deteksi blob pada gambar asli tanpa noise
blobs_asli = blob_log(gambar_asli_tanpa_noise, min_sigma=17, max_sigma=4, num_sigma=1, threshold=5)

# Lakukan operasi lebih lanjut seperti yang telah Anda lakukan sebelumnya dengan hasil deteksi blob
# Misalnya, menambahkan lingkaran pada citra

# Tampilkan hasilnya
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,23))
ax1.imshow(biner, cmap='gray')
ax1.set_title('Gambar Kecil Tanpa Noise')
for blob in blobs_kecil:
    y, x, s = blob
    ax1.add_patch(plt.Circle((x, y), s, color='r', fill=False))

ax2.imshow(gambar_asli_tanpa_noise, cmap='gray')
ax2.set_title('Gambar Asli Tanpa Noise')
for blob in blobs_asli:
    y, x, s = blob
    ax2.add_patch(plt.Circle((x, y), s, color='r', fill=False))

plt.show()

count_kecil = len(blobs_kecil)
count_asli = len(blobs_asli)

print("Jumlah blob pada gambar kecil tanpa noise:", count_kecil)
print("Jumlah blob pada gambar asli tanpa noise:", count_asli)
