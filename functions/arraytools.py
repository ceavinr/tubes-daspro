alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialchar = ['_', '-', ' ', '@', '%', '+', '/', '!', '#', '$', '?', ':', '.', '(',
               ')', '~', '^', '&', '*', '=', '{', '[', '}', ']', '|', '<', '>']


def panjang(arr):
    # Fungsi yang menerima sebuah array dan menghitung panjang array tersebut

    # KAMUS LOKAL
    # pjg : integer

    # ALGORITMA
    pjg = 0

    for _ in arr:       # Setiap membaca ada sebuah elemen dalam array, nilai pjg bertambah 1
        pjg += 1

    return pjg


def splitting(string, delimiter=";"):
    # Memisahkan delimiter dari string

    # KAMUS LOKAL
    # temp : string
    # data : array

    # ALGORITMA
    temp = ""           # Variabel sementara untuk menampung anggota list
    data = []           # List untuk menampung data

    for char in string:     # Looping setiap huruf yang ada pada string
        if char == "\n":
            data += [temp]
            temp = ""
        elif char == delimiter:
            data += [temp]  # Menambahkan variabel sementara ke dalam list data
            temp = ""       # Mengosongkan variabel sementara
        else:
            temp += char    # Menambahkan huruf ke dalam variabel sementara
    if temp:
        data += [temp]      # Menambahkan sisa string ke dalam list data dalam bentuk integer

    return data


def joining(arr, delimiter=";"):
    # Menggabungkan anggota dalam list menjadi sebuah string dengan delimiter tertentu

    # KAMUS LOKAL
    # string : str

    # Menambahkan string dan delimiter secara bergantian ke dalam string
    string = str(arr[0])
    for i in range(1, panjang(arr)):
        string += delimiter
        string += str(arr[i])

    return string


def find_index_matriks(element, arr, idx):
    # Mencari indeks pertama ditemukan element dalam sebuah array dalam sebuah matriks.
    # Jika tidak ditemukan, maka fungsi mereturn -999

    # KAMUS LOKAL

    # ALGORITMA
    for i in range(panjang(arr)):
        if element == arr[i][idx]:
            return i
    return -999


def find_index_array(element, arr):
    # Mencari indeks pertama ditemukan element dalam sebuah array.
    # Jika tidak ditemukan, maka fungsi mereturn -999

    # KAMUS LOKAL

    # ALGORITMA
    for i in range(panjang(arr)):
        if element == arr[i]:
            return i
    return -999


def update_data(new, old):
    # Fungsi untuk mengupdate data pada indeks suatu array

    # KAMUS LOKAL

    # ALGORITMA
    if new == '':        # Jika update kosong, data tetap sama
        return old
    else:                   # Jika update tidak kosong, data diganti dengan update terbaru
        return new


def is_subset(arr1, arr2):
    # Fungsi yang mereturn True jika arr1 merupakan subset dari arr2
    # elemen pada list allowed

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA
    count = 0

    # Mengecek apakah setiap karakter pada username valid (terdapat pada list allowed)
    for i in range(panjang(arr1)):
        if arr1[i] in arr2:
            count += 1

    return count == panjang(arr1)


def right_strip(string, toRemove=" "):
    # Menghilangkan trailing character pada string sesuai argumen saat memanggil fungsi

    # KAMUS LOKAL
    # new_str, temp : string

    # ALGORITMA
    new_str = ""
    temp = ""

    for char in string:
        temp += char
        if char == toRemove:
            continue
        elif char != toRemove:              # Jika karakter-karakter awal bukan lagi yang ingin dihilangkan
            new_str += temp                 # new_str diisi dengan string yang sudah ditampung pada temp
            temp = ""

    return new_str


def left_strip(string, toRemove=" "):
    # Menghilangkan leading character pada string sesuai argumen saat memanggil fungsi

    # KAMUS LOKAL
    # new_str : string
    # temp : integer

    # ALGORITMA
    new_str = ""
    temp = 0            # Variabel untuk menyimpan indeks pertama kali karakter bukan lagi yang ingin dihilangkan
    for i in range(panjang(string)):
        if string[i] == toRemove:
            temp = i+1
        else:
            break           # Loop berhenti jika karakter-karakter awal bukan spasi

    for char in range(temp, panjang(string)):   # Looping hanya dimulai dari indeks setelah karakter yang ingin dihilangkan
        new_str += string[char]

    return new_str


def stripping(string, toRemove=" "):
    # Menghilangkan leading dan trailing character pada string sesuai argumen saat memanggil fungsi

    # KAMUS LOKAL

    # ALGORITMA
    new_str = left_strip(right_strip(string, toRemove), toRemove)

    return new_str


def search_by(element, by, arr):
    # Mencari elemen dalam sebuah array dalam sebuah matriks. Jika ditemukan, fungsi akan mereturn array di mana
    # elemen tersebut ditemukan. Jika tidak, fungsi mereturn array kosong. Jika elemen kosong fungsi akan mereturn array
    # kosong

    # KAMUS LOKAL
    # found : array

    # ALGORITMA
    found = []
    if element == "":       # Jika elemen kosong fungsi akan mereturn array kosong
        return arr
    else:
        for i in range(panjang(arr)):
            if element == arr[i][by]:   # Jika elemen ditemukan, array terkait akan diitambahkan ke dalam variabel found
                found += [arr[i]]

    return found


def popped(arr, pop_index):
    # Mereturn array yang elemen pada index tertentunya sudah dihilangkan

    # KAMUS LOKAL
    # new_arr : array

    # ALGORITMA
    new_arr = []
    for i in range(panjang(arr)):
        if pop_index < 0:                       # Jika menggunakan indexing integer negatif
            if i == panjang(arr)+pop_index:     # Pada saat pencacah sama dengan index, loop diskip
                continue
        else:  # pop_index >= 0
            if i == pop_index:                  # Pada saat pencacah sama dengan index, loop diskip
                continue
        new_arr += [arr[i]]                     # Menambahkan elemen demi elemen ke dalam new_arr

    return new_arr


def selection_sorted(matrix, by, ascending=True):
    # Menyusun array berdasarkan nilai pada kolom tertentu dengan teknik selection sort

    # KAMUS LOKA
    # iMin, iMax : integer

    # ALGORITMA
    if ascending:
        for i in range(panjang(matrix)):
            iMin = i                                            # Inisialisasi nilai index nilai minimum
            for j in range(i, panjang(matrix)):
                if matrix[iMin][by] > matrix[j][by]:            # Jika nilai di indeks j lebih kecil, ganti nilai iMin
                    iMin = j
            matrix[iMin], matrix[i] = matrix[i], matrix[iMin]   # Tukar elemen pada i dengan elemen pada iMin
    else:
        for i in range(panjang(matrix)):
            iMax = i                                            # Inisialisasi nilai index nilai maksimum
            for j in range(i, panjang(matrix)):
                if matrix[iMax][by] < matrix[j][by]:            # Jika nilai di indeks j lebih besar, ganti nilai iMax
                    iMax = j
            matrix[iMax], matrix[i] = matrix[i], matrix[iMax]   # Tukar elemen pada i dengan elemen pada iMax

    return matrix


def extract_integer(string):
    # Mengambil elemen bilangan dari string dengan format GAMEXXX

    # KAMUS LOKAL
    # ratusan, puluhan, satuan : integer

    # ALGORITMA
    ratusan = int(string[-3]) * 100
    puluhan = int(string[-2]) * 10
    satuan = int(string[-1])

    return ratusan + puluhan + satuan
