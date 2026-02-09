#!/usr/bin/env python3
"""
Script untuk scraping data berita dari file XML
Indonesian News Corpus - Analisis Sentimen Berita

Tugas: Scraping data berita menggunakan BeautifulSoup
Output: DataFrame pandas dan file CSV
"""

from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_xml_berita(file_path):
    """
    Fungsi untuk parsing file XML berita dan ekstrak informasi
    
    Args:
        file_path: Path ke file XML
        
    Returns:
        DataFrame pandas dengan data berita
    """
    print(f"📖 Membaca file: {file_path}")
    
    # Baca file XML
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse dengan BeautifulSoup
    soup = BeautifulSoup(content, 'xml')
    
    # Cari semua tag berita
    berita_list = soup.find_all('berita')
    print(f"✅ Ditemukan {len(berita_list)} berita")
    
    # List untuk menyimpan data
    data = []
    
    # Ekstrak data dari setiap berita
    for idx, berita in enumerate(berita_list, 1):
        try:
            item = {
                'id': idx,
                'sumber': berita.find('sumber').text if berita.find('sumber') else '',
                'tanggal': berita.find('tanggal').text if berita.find('tanggal') else '',
                'kategori': berita.find('kategori').text if berita.find('kategori') else '',
                'judul': berita.find('judul').text if berita.find('judul') else '',
                'isi': berita.find('isi').text if berita.find('isi') else '',
                'link': berita.find('link').text if berita.find('link') else '',
                'jumlah_kata': int(berita.find('jumlahkata').text) if berita.find('jumlahkata') and berita.find('jumlahkata').text else 0
            }
            data.append(item)
            
            # Progress indicator setiap 100 berita
            if idx % 100 == 0:
                print(f"   Memproses: {idx}/{len(berita_list)} berita...")
                
        except Exception as e:
            print(f"⚠️  Error pada berita #{idx}: {e}")
            continue
    
    # Buat DataFrame
    df = pd.DataFrame(data)
    
    print(f"\n✅ Berhasil mengekstrak {len(df)} berita")
    return df


def analisis_data(df):
    """Tampilkan statistik data"""
    print("\n" + "="*60)
    print("📊 STATISTIK DATA")
    print("="*60)
    
    print(f"\nTotal berita: {len(df)}")
    print(f"\nKategori berita:")
    print(df['kategori'].value_counts())
    
    print(f"\nSumber berita:")
    print(df['sumber'].value_counts())
    
    print(f"\nStatistik jumlah kata:")
    print(df['jumlah_kata'].describe())
    
    print("\n" + "="*60)


def main():
    """Fungsi utama"""
    print("="*60)
    print("🔍 SCRAPING BERITA - Indonesian News Corpus")
    print("="*60)
    print()
    
    # File XML yang akan di-scrape
    xml_file = '/home/ubuntu/.clawdbot/media/inbound/be974e93-1b50-4cf4-bcf1-f509bed5be10'
    
    # Scraping data
    df = scrape_xml_berita(xml_file)
    
    # Analisis data
    analisis_data(df)
    
    # Simpan ke CSV
    output_csv = 'hasil_scraping_berita.csv'
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"\n💾 Data berhasil disimpan ke: {output_csv}")
    
    # Tampilkan preview 5 berita pertama
    print("\n" + "="*60)
    print("👀 PREVIEW 5 BERITA PERTAMA")
    print("="*60)
    print()
    print(df[['id', 'sumber', 'kategori', 'judul']].head())
    
    print("\n" + "="*60)
    print("✨ SELESAI!")
    print("="*60)
    
    return df


if __name__ == '__main__':
    df_berita = main()
