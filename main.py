"""
Aplikasi Deteksi Gempa

"""


def ekstrasi_data():
    """

    Tanggal     :   05 September 2022
    Waktu       :   10:17:29 WIB
    Magnitude   :   4.6
    Kedalaman   :   31 km
    Lokasi      :   5.76 LS - 103.91 BT
    Keterangan  :   Pusat gempa berada di laut 63 km baratdaya Pesisir Barat
    Skala MMI   :   Dirasakan II-III Liwa, II Pesisir Barat

    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '5 September 2022'
    hasil['waktu'] = '10:17:29 WIB'
    hasil['magnitudo'] = 4.6
    hasil['kedalaman'] = 31
    hasil['lokasi'] = {'ls': 5.76 , 'bt': 103.91}
    hasil['pusat'] = 'Pusat gempa berada di laut 63 km baratdaya Pesisir Barat'
    hasil['skalammi'] = 'Dirasakan II-III Liwa, II Pesisir Barat'


    return hasil



def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG\n')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan (Skala MMI): {result['skalammi']}")



if __name__ == '__main__':
    print("Aplikasi Utama")
    result = ekstrasi_data()
    tampilkan_data(result)
    
