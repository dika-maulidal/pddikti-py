import argparse
from pddiktipy import api
from colorama import Fore, Style, init

# Inisialisasi API
a = api()

# Inisialisasi Colorama
init(autoreset=True)

# Custom ArgumentParser untuk mengubah warna usage
class CustomArgumentParser(argparse.ArgumentParser):
    def format_usage(self):
        return Fore.LIGHTBLUE_EX + super().format_usage() + Style.RESET_ALL

# Fungsi untuk menampilkan ASCII art
def display_ascii_art():
    print()
    print(Fore.LIGHTBLUE_EX + "       _.-'`'-._")
    print(Fore.LIGHTBLUE_EX + "    .-'    _    '-.")
    print(Fore.LIGHTBLUE_EX + "     `-.__  `\_.-'")
    print(Fore.LIGHTBLUE_EX + "       |  `-``\|")
    print(Fore.LIGHTBLUE_EX + "       `-.....-A")
    print(Fore.LIGHTBLUE_EX + "               #")
    print(Fore.LIGHTBLUE_EX + "               #")

# Fungsi untuk merapikan hasil pencarian mahasiswa
def format_mahasiswa_result(result, search_term):
    formatted = []
    for item in result.get('mahasiswa', []):
        text_parts = item['text'].split(', ')
        name = text_parts[0].strip()
        if search_term.lower() in name.lower():
            university = text_parts[1].split(': ')[1]
            prodi = text_parts[2].split(': ')[1]
            formatted.append({
                "nama": name,
                "universitas": university,
                "prodi": prodi
            })
    return formatted

# Fungsi untuk merapikan hasil pencarian universitas
def format_university_result(result, search_term):
    formatted = []
    for item in result:
        text_parts = item['text'].split(', ')
        name = text_parts[0].split(': ')[1].strip()
        if search_term.lower() in name.lower():
            npsn = text_parts[1].split(': ')[1].strip()
            abbreviation = text_parts[2].split(': ')[1].strip() if len(text_parts) > 2 else ""
            address = text_parts[3].split(': ')[1].strip() if len(text_parts) > 3 else ""
            formatted.append({
                "nama": name,
                "npsn": npsn,
                "singkatan": abbreviation,
                "alamat": address
            })
    return formatted

# Fungsi untuk merapikan hasil pencarian dosen
def format_dosen_result(result, search_term):
    formatted = []
    for item in result:
        text_parts = item['text'].split(', ')
        name = text_parts[0].strip()
        if search_term.lower() in name.lower():
            nidn = text_parts[1].split(': ')[1]
            universitas = text_parts[2].split(': ')[1]
            prodi = text_parts[3].split(': ')[1]
            formatted.append({
                "nama": name,
                "nidn": nidn,
                "universitas": universitas,
                "prodi": prodi
            })
    return formatted

def main():
    # Tampilkan ASCII art
    display_ascii_art()

    # Argument parser untuk mengambil input dari command line
    parser = CustomArgumentParser(description=Fore.LIGHTBLUE_EX + 'Cari data mahasiswa, perguruan tinggi, atau dosen dari PDDIKTI.',
                                  formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-m', '--mahasiswa', type=str, help=Fore.LIGHTBLUE_EX + 'Nama mahasiswa yang ingin dicari')
    parser.add_argument('-u', '--university', type=str, help=Fore.LIGHTBLUE_EX + 'Nama perguruan tinggi yang ingin dicari')
    parser.add_argument('-d', '--dosen', type=str, help=Fore.LIGHTBLUE_EX + 'Nama dosen yang ingin dicari')
    args = parser.parse_args()

    if args.mahasiswa:
        search_term = args.mahasiswa
        print()
        print(Fore.LIGHTBLUE_EX + f"[+] Checking '{search_term}' on PDDIKTI :")
        print("===================================================")
        print(Fore.WHITE + Style.BRIGHT + f"                   {search_term}")
        print("===================================================")

        # Cari mahasiswa
        result = a.search_mahasiswa(search_term)

        # Gunakan fungsi untuk merapikan hasil
        formatted_result = format_mahasiswa_result(result, search_term)

        # Cetak hasil yang sudah dirapikan atau pesan jika tidak ditemukan
        if formatted_result:
            for mahasiswa in formatted_result:
                print(Fore.LIGHTBLUE_EX + f"Nama: {mahasiswa['nama']}")
                print(Fore.LIGHTBLUE_EX + f"Universitas: {mahasiswa['universitas']}")
                print(Fore.LIGHTBLUE_EX + f"Prodi: {mahasiswa['prodi']}")
                print()
        else:
            print(Fore.RED + "Mahasiswa tidak ditemukan.")

    elif args.university:
        search_term = args.university
        print()
        print(Fore.LIGHTBLUE_EX + f"[+] Checking '{search_term}' on PDDIKTI :")
        print("===================================================")
        print(Fore.WHITE + Style.BRIGHT + f"                   {search_term}")
        print("===================================================")

        # Cari perguruan tinggi
        result = a.search_pt(search_term)

        # Gunakan fungsi untuk merapikan hasil
        formatted_result = format_university_result(result, search_term)

        # Cetak hasil yang sudah dirapikan atau pesan jika tidak ditemukan
        if formatted_result:
            for pt in formatted_result:
                print(Fore.LIGHTBLUE_EX + f"Nama: {pt['nama']}")
                print(Fore.LIGHTBLUE_EX + f"NPSN: {pt['npsn']}")
                print(Fore.LIGHTBLUE_EX + f"Singkatan: {pt['singkatan']}")
                print(Fore.LIGHTBLUE_EX + f"Alamat: {pt['alamat']}")
                print()
        else:
            print(Fore.RED + "Perguruan tinggi tidak ditemukan.")

    elif args.dosen:
        search_term = args.dosen
        print()
        print(Fore.LIGHTBLUE_EX + f"[+] Checking '{search_term}' on PDDIKTI :")
        print("===================================================")
        print(Fore.WHITE + Style.BRIGHT + f"                   {search_term}")
        print("===================================================")

        # Cari dosen
        result = a.search_dosen(search_term)

        # Gunakan fungsi untuk merapikan hasil
        formatted_result = format_dosen_result(result, search_term)

        # Cetak hasil yang sudah dirapikan atau pesan jika tidak ditemukan
        if formatted_result:
            for dosen in formatted_result:
                print(Fore.LIGHTBLUE_EX + f"Nama: {dosen['nama']}")
                print(Fore.LIGHTBLUE_EX + f"NIDN: {dosen['nidn']}")
                print(Fore.LIGHTBLUE_EX + f"Universitas: {dosen['universitas']}")
                print(Fore.LIGHTBLUE_EX + f"Prodi: {dosen['prodi']}")
                print()
        else:
            print(Fore.RED + "Dosen tidak ditemukan.")

    else:
        print(Fore.LIGHTBLUE_EX + "Silakan masukkan argumen -m untuk mencari mahasiswa, -u untuk mencari perguruan tinggi, atau -d untuk mencari dosen.")

if __name__ == '__main__':
    main()
