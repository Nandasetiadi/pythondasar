import os
import time

def main():
    print("Selamat datang di Hotel VANDERBOB")

    while True:
        # harga dan tipe kamar
        saldo = 0  # Initialize saldo
        print("\nTipe Kamar:")
        kamar1 = ["1-2 hari  100.000/night", "3-4 hari  90.000/night", ">=5 hari  80.000/night"]
        kamar2 = ["2. Deluxe", "1-2 hari 150.000/night", "3-4 hari 135.000/night", ">=5 hari 120.000/night"]
        kamar3 = ["3. Premium", "1-2 hari 200.000/night", "3-4 hari 180.000/night", ">=5 hari  160.000/night"]
        # memunculkan harga
        print("1. Superior")
        for a in kamar1:
            print(a)
        print("----------------------")
        for a in kamar2:
            print(a)
        print("----------------------")
        for a in kamar3:
            print(a)
        print("----------------------")
        # input nama, nomor KTP, dan tipe
        nama = input("Masukkan nama anda: ")
        nomor_ktp = input("Masukkan nomor KTP: ")
        tipe_kamar = int(input("Pilih tipe kamar (1/2/3) atau 0 untuk keluar: "))

        # Meminta input lama menginap
        lama_menginap = int(input("Masukkan lama menginap (jumlah hari): "))

        # total awal harga dan nama tipe
        harga_per_hari = 0
        nama_tipe_kamar = ""

        # Menghitung harga dan menentukan nama tipe kamar
        if tipe_kamar == 0:
            print("\nTerima kasih telah menggunakan layanan kami.")
            break
        elif tipe_kamar == 1:
            if lama_menginap == 2 or lama_menginap == 1 :
                harga_per_hari = 100000
            elif lama_menginap == 3 or lama_menginap == 4:
                harga_per_hari = 90000
            elif lama_menginap >= 5:
                harga_per_hari = 80000
            nama_tipe_kamar = "Superior"
        elif tipe_kamar == 2:
            if lama_menginap == 2 or lama_menginap == 1 :
                harga_per_hari = 150000
            elif lama_menginap == 3 or lama_menginap == 4:
                harga_per_hari = 135000
            elif lama_menginap >= 5:
                harga_per_hari = 120000
            nama_tipe_kamar = "Deluxe"
        elif tipe_kamar == 3:
            if lama_menginap == 2 or lama_menginap == 1:
                harga_per_hari = 200000
            elif lama_menginap == 3 or lama_menginap == 4:
                harga_per_hari = 180000
            elif lama_menginap >= 5:
                harga_per_hari = 160000
            nama_tipe_kamar = "Premium"
        else:
            print("Pilihan tipe kamar tidak valid.")
            print("mohon mengulang kembali")
            continue
        # total harga dan penambahan pajak
        total_harga = harga_per_hari * lama_menginap
        ppn = 10
        ppn_total = total_harga / ppn

        # Hitung diskon
        diskon = 0
        if lama_menginap >= 10 and lama_menginap < 20:
            diskon = 0.2  # 20% diskon
        elif lama_menginap >= 20 and lama_menginap < 30:
            diskon = 0.3  # 30% diskon
        elif lama_menginap >= 30:
            diskon = 0.4  # 40% diskon

        total_diskon = total_harga * diskon
        total_harga_setelah_diskon = total_harga - total_diskon

        total_ppn = total_harga_setelah_diskon / ppn

        pilih = ["1.debit","2.tunai"]
        for a in pilih:
            print (a)
        d = int(input("pilih metode pembayaran(1/2)"))

        bank = int(input("Masukkan uang anda: "))
        saldo += bank
        if bank <= total_harga:
            print("maaf saldo anda tidak mencukupi untuk melakukan pembayaran harap coba lagi")
            continue
        # hasil pembayaran
        print("\nRincian Pembayaran:")
        print("Nama: " + nama)
        print("Nomor KTP: " + nomor_ktp)
        print("Tipe Kamar: " + nama_tipe_kamar)
        print(f"Harga per Hari: Rp.{harga_per_hari}")
        print(f"Lama Menginap: {lama_menginap} hari")
        print(f"Total Harga: Rp.{total_harga_setelah_diskon}")
        print(f"Pajak: Rp.{ppn_total}")
        print(f"Diskon: Rp.{total_diskon} ({diskon*100:.0f}%)")
        saldo -= total_harga  # mengambil total harga dari saldo

        print(f"\nSaldo Anda Sekarang: Rp.{saldo}")

        # pengulangan program dari awal
        more = str(input("apakah anda ingin mengulang kembali? : (yes/no) "))
        if more == "no":
            print("\nTerima kasih telah menggunakan layanan kami.")
            break

if __name__ == "__main__":
    main()
