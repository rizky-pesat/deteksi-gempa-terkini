import requests
from bs4 import BeautifulSoup


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
    try :
        content = requests.get('https://bmkg.go.id/')
    except Exception :
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.string)
        taktu = soup.find('span', {'class': 'waktu'})
        taktu = taktu.text.split(', ')
        tanggal = taktu[0]
        waktu = taktu[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = 0
        ls = 0
        bt = 0

        for res in result:
            #print(i, res)
            if i == 1:
                magnitude = res.text
            elif i == 2:
                dalam = res.text
            elif i == 3:
                koor = res.text.split(' - ')
                ls = koor[0]
                bt = koor[1]
            elif i == 4 :
                lokasi = res.text
            elif i == 5 :
                dirasakan = res.text

            i = i + 1




    # print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = tanggal
    hasil['waktu'] = waktu
    hasil['magnitudo'] = magnitude
    hasil['kedalaman'] = dalam
    hasil['lokasi'] = {'ls': ls , 'bt': bt}
    hasil['pusat'] = lokasi
    hasil['skalammi'] = dirasakan


    return hasil



def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menampilkan gempa terkini")
        return

    print('Gempa Terakhir Berdasarkan BMKG\n')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan (Skala MMI): {result['skalammi']}")

# if __name__ == '__main__':
#     print("Aplikasi Dashboard")