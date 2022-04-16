import os
import time
import interface
from functions.formulas import linear_congruential
from functions.arraytools import panjang


def kerangajaib():
    # Mensimulasikan magic conch shell
    # I.S. Array replies terdefinisi
    # F.S. Ditampilkan jawaban yang diambil dari array replies secara pseudorandom

    # KAMUS LOKAL
    # replies : array of string

    # ALGORITMA
    os.system("cls")
    replies = ["hah", "gatau", "iyah", "hmm", "g"]  # List jawaban yang bisa dikeluarkan

    second = time.gmtime().tm_sec                   # Mengambil detik hari ini untuk dipakai sebagai seed
    randomIndex = linear_congruential(panjang(replies), second)

    print("Apa pertanyaanmu?")
    input(">>> ")

    interface.gambar_kerang("[green]{}[/green]".format(replies[randomIndex]))

    return
