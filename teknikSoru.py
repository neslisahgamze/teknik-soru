saatler=[
    {'kota':3,'saat':'09:00'},
    {'kota':3,'saat':'09:20'},
    {'kota':3,'saat':'09:40'},
    {'kota':3,'saat':'10:00'},
    {'kota':3,'saat':'10:20'},
    {'kota':3,'saat':'10:40'},
    {'kota':2,'saat':'11:00'},
    {'kota':2,'saat':'11:20'},
    {'kota':2,'saat':'11:40'}

]
randevular=[
    {'kisi_sayisi':2,'saat':'10:40'},
    {'kisi_sayisi':3,'saat':'09:00'},
    {'kisi_sayisi':1,'saat':'11:40'},
    {'kisi_sayisi':2,'saat':'11:20'},
    {'kisi_sayisi':1,'saat':'09:40'},
    {'kisi_sayisi':3,'saat':'09:00'},
    {'kisi_sayisi':4,'saat':'10:00'}
]

def dagit():
    for i in range(0,len(randevular)):
        kisiSayisi = randevular[i]['kisi_sayisi']
        saat = randevular[i]['saat']
        for j in range(0,len(saatler)):
            if(saatler[j]['saat'] == randevular[i]['saat']):
                for k in range (0,kisiSayisi):
                    saatler[j+k]['kota'] = saatler[j+k]['kota']-1

def musait_saatler(saatler, randevular, kisi):
    kontrol = True
    musaitSaatler = []
    for j in range(0,len(saatler)):
        if(j+kisi <= len(saatler)-1):
            for k in range (0,kisi):
                if((saatler[j+k]['kota'] > 0)):
                    continue
                else:
                    kontrol = False
                    break
            if(kontrol == True):
                musaitSaatler.append(saatler[j]['saat'])
            kontrol = True
    return musaitSaatler

def main():
    kisi = input("Kisi sayisini giriniz: ")
    dagit()
    """for z in saatler:
        print(z)
    """
    uygun = musait_saatler(saatler, randevular, int(kisi))
    print(uygun)

main()
