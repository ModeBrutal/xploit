# Xploit Framework

Xploit Framework adalah alat multifungsi yang dikembangkan oleh **X'Boy Linux** untuk pengujian keamanan dan eksploitasi. Framework ini memiliki berbagai tools seperti WHOIS Lookup, IP Lookup, DNS Lookup, CMS Detection, HTTP Flood (DoS), dan lainnya.

## Fitur Utama
- **WHOIS Lookup**: Untuk memperoleh informasi tentang domain.
- **IP Lookup**: Mendapatkan informasi tentang alamat IP.
- **DNS Lookup**: Melakukan pencarian DNS untuk domain.
- **CMS Detection**: Mendeteksi platform CMS dari website.
- **HTTP Flood (DoS)**: Mengirimkan request untuk melakukan serangan DDoS.
- **GeoIP Lookup**: Mengetahui lokasi berdasarkan IP.

## Cara Menggunakan
1. Clone repository ini:
   ```bash
   git clone https://github.com/username/Xploit-Framework.git
   ```
2. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan alat menggunakan file Python:
   ```bash
   python xploit_framework.py
   ```

## Instalasi
Framework ini membutuhkan Python 3.x dan beberapa dependensi. Untuk menginstalnya, jalankan perintah berikut:
```bash
pip install requests whois dns.resolver colorama
