# LAPORAN WEB SCRAPING
## Analisis Sentimen Terhadap Berita di Indonesian News Corpus

---

### 📋 INFORMASI TUGAS

**Nama Kelompok:** (Isi sesuai nama kelompok)  
**Tema:** Analisis Sentimen terhadap berita di Indonesian News Corpus  
**Tools:** Python, BeautifulSoup4, Pandas  
**Tanggal:** 9 Februari 2026

---

### 🎯 PERMASALAHAN

Menganalisis sentimen terhadap berita-berita yang terdapat di Indonesian News Corpus yang tersimpan dalam format XML. Data berita perlu diekstrak dan dianalisis untuk mengetahui pola kategori, sumber, dan distribusi berita.

---

### 📊 DATA YANG DIBUTUHKAN

Dari file XML Indonesian News Corpus, data yang diekstrak meliputi:

1. **ID** - Nomor urut berita
2. **Sumber** - Website sumber berita (kompas.com, merdeka.com, dll)
3. **Tanggal** - Tanggal publikasi berita
4. **Kategori** - Kategori berita (Teknologi, Bola, Nasional, dll)
5. **Judul** - Judul berita
6. **Isi** - Konten/isi berita lengkap
7. **Link** - URL berita
8. **Jumlah Kata** - Jumlah kata dalam berita

**Sumber Data:** File XML Indonesian News Corpus

---

### 🛠️ PROSES SCRAPING

#### Tools yang Digunakan:
- **Python 3** - Bahasa pemrograman
- **BeautifulSoup4** - Library untuk parsing XML/HTML
- **lxml** - XML parser
- **Pandas** - Library untuk manipulasi dan analisis data

#### Langkah-langkah:

1. **Import Library**
```python
from bs4 import BeautifulSoup
import pandas as pd
```

2. **Baca File XML**
```python
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
```

3. **Parse dengan BeautifulSoup**
```python
soup = BeautifulSoup(content, 'xml')
berita_list = soup.find_all('berita')
```

4. **Ekstrak Data dari Setiap Berita**
```python
for berita in berita_list:
    item = {
        'id': idx,
        'sumber': berita.find('sumber').text,
        'tanggal': berita.find('tanggal').text,
        'kategori': berita.find('kategori').text,
        'judul': berita.find('judul').text,
        'isi': berita.find('isi').text,
        'link': berita.find('link').text,
        'jumlah_kata': int(berita.find('jumlahkata').text)
    }
```

5. **Buat DataFrame Pandas**
```python
df = pd.DataFrame(data)
```

6. **Export ke CSV**
```python
df.to_csv('hasil_scraping_berita.csv', index=False, encoding='utf-8')
```

---

### 📈 HASIL SCRAPING

#### Statistik Data:

**Total Berita Berhasil Diekstrak:** 1,348 berita

#### Distribusi per Kategori:
| Kategori | Jumlah |
|----------|--------|
| Nasional | 468 |
| Bola | 352 |
| Bisnis Ekonomi | 246 |
| Lifestyle | 68 |
| Otomotif | 64 |
| Teknologi | 62 |
| Olahraga | 53 |
| Travel | 35 |

#### Distribusi per Sumber:
| Sumber | Jumlah |
|--------|--------|
| republika.co.id | 394 |
| viva.co.id | 292 |
| tribunnews.com | 271 |
| merdeka.com | 235 |
| kompas.com | 156 |

#### Statistik Jumlah Kata:
- **Mean (Rata-rata):** 181 kata
- **Min:** 2 kata
- **Max:** 941 kata
- **Median:** 176.5 kata

---

### 📁 OUTPUT

#### File yang Dihasilkan:

1. **scrape_berita.py** - Script Python untuk scraping
2. **hasil_scraping_berita.csv** - Data hasil scraping dalam format tabulasi (CSV)
   - Ukuran: 2.0 MB
   - Jumlah Baris: 1,349 (termasuk header)
   - Format: CSV dengan encoding UTF-8

#### Preview Data (5 Berita Pertama):

| ID | Sumber | Kategori | Judul |
|----|--------|----------|-------|
| 1 | kompas.com | Teknologi | 20 Tahun Lalu, Inilah Kehebohan Peluncuran Windows 95 |
| 2 | kompas.com | Teknologi | Kurangi Jualan Ponsel, BlackBerry Malah Untung |
| 3 | kompas.com | Teknologi | Data Center Google Setelah Tersambar Petir |
| 4 | kompas.com | Teknologi | Perbedaan RAM Tidak Menurunkan Performa Oppo R7 Lite |
| 5 | kompas.com | Teknologi | Dollar Menguat, Cuma 3 Merek Ponsel yang Naik Harga |

---

### 💡 INSIGHT

1. **Kategori Nasional** mendominasi dengan 468 berita (34.7% dari total)
2. **Republika.co.id** adalah sumber terbanyak dengan 394 berita
3. Rata-rata panjang berita adalah **181 kata**, menunjukkan berita-berita cenderung ringkas
4. Berita terpendek hanya 2 kata, sementara terpanjang mencapai 941 kata
5. **Teknologi dan Olahraga** memiliki porsi cukup signifikan dalam korpus berita

---

### 🎓 KESIMPULAN

Proses web scraping dari file XML Indonesian News Corpus berhasil dilakukan dengan sempurna menggunakan kombinasi BeautifulSoup4 dan Pandas. Total 1,348 berita berhasil diekstrak dan disimpan dalam format CSV yang siap untuk analisis lebih lanjut, terutama untuk analisis sentimen.

Data yang diperoleh menunjukkan distribusi yang beragam dari berbagai kategori dan sumber berita, dengan dominasi berita nasional dan kontribusi terbesar dari republika.co.id.

---

### 📚 REFERENSI

- BeautifulSoup4 Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Indonesian News Corpus: Dataset berita berbahasa Indonesia

---

**Dibuat dengan:** Python 3, BeautifulSoup4, Pandas  
**Tanggal:** 9 Februari 2026
