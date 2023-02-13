##AY EVRESİ HESAPLAMA ARACI
# AŞAĞIDAKİ RUN TUŞUNA BASARAK ÇALIŞTIRINIZ İSTEDİĞİNİZ TARİHİ GİRİNİZ ÖRN : YIL: 2003  AY: 03 GÜN: 15
#                                      |
#                                      |
#                                      |
#                                      |
#                                      ↓
#
from browser import document, window, alert
year = int(input("Hesaplamak istediğiniz yıl=="))
month = int(input("Hesaplamak istediğiniz ay=="))
day = int(input("Hesaplamak istediğiniz gün=="))


def moon_phase(month, day, year):
    ages = [
        18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7
    ]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = [
        "Yeni Ay", "Yeni Ay", "İlk Dördün", "İlk Dördün", "Dolunay", "Dolunay",
        "Son dördün", "Son Dördün"
    ]
    months = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"
    ]

    if day == 31:
        day = 1
    days_into_phase = ((ages[(year + 1) % 19] +
                        ((day + offsets[month - 1]) % 30) + (year < 1900)) %
                       30)
    index = int((days_into_phase + 2) * 16 / 59.0)
    #print(index)  # test
    if index > 7:
        index = 7
    status = description[index]

    # light should be 100% 15 days into phase
    light = int(2 * days_into_phase * 100 / 29)
    if light > 100:
        light = abs(light - 200)
    date = "%d%s%d" % (day, months[month - 1], year)

    return date, status, light


date, status, light = moon_phase(month, day, year)
print("%s tarihinde Ay Evresi %s, Görünürlük yüzdedsi = %d%s" %
      (date, status, light, '%'))
