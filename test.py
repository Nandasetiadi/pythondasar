import time
import os

def input_numbers():
    numbers = []
    for i in range(5):
        num = int(input("Masukkan angka ke-{}: ".format(i + 1)))
        numbers.append(num)
    return numbers

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    while True:
        os.system('cls')
        start_time = time.time()
        print("===== Program Pengurutan Angka =====")
        numbers = input_numbers()

        sorting_option = input("Pilih pengurutan (ascending/descending): ").lower()

        if sorting_option == "ascending" or "asc" :
            bubbleSort(numbers)
        elif sorting_option == "descending" or "dsc":
            bubbleSort(numbers)
            numbers.reverse()
        else:
            print("Pilihan pengurutan tidak valid.")
            continue
        
        max_num = max(numbers)
        min_num = min(numbers)
        average = sum(numbers) / len(numbers)

        print("<=============================================>")
        print("Hasil pengurutan ({}): {}".format(sorting_option, numbers))
        print("Angka max:", max_num)
        print("Angka min:", min_num)
        print("Rata-rata:", average)

        end_time = time.time()
        execution_time = end_time - start_time
        print("Waktu yang diperlukan:", execution_time, "detik")
        print("<=============================================>")

        repeat = input("Ingin ulang? (yes/no)? ").lower()
        if repeat == "yes" or repeat == "y":
            continue
        elif repeat == "no" or repeat == "n":
            print("Terima kasih, dan Selamat tinggal!")
            break
        else:
            print("Masukan tidak valid. Program berakhir.")
            break
        

if __name__ == "__main__":
    main()
