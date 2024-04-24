# failas = open("naujasFailas.txt","a",encoding="utf8")
# print(failas.write("ožėlis mažasis\n"))
# failas.close()
import random

# failas = open("naujasFailas.txt","r",encoding="utf8")
# print(failas.readlines())
# failas.close()
#
# failas = open("naujasFailas.txt","r",encoding="utf8")
# for line in failas.readlines():
#     print(line)
# failas.close()
#
#
# with open("naujasFailas.txt", "r",encoding="utf8") as failas:
#     lines = failas.read().split("\n")
#     for line in lines:
#         print(line)
#
#
#
# def formatName(name):
#     res = ""
#     for part in name.split(" "):
#         res += str(part[0]).upper() + str(part[1:]).lower() + " "
#     return res[:-1]
#
# print(formatName("naglis jonas"))
# print(formatName("Naglis jonas"))
# print(formatName("nAGLIS jONAS"))
#
#
#
# text = "labas rytas grazus oras"
# print(text)
# print(text.split("s"))
# for txt in text.split("s"):
#     if txt != "":
#         print("|" + txt + "|")
#
# for i in range(1):
#     skaiciukasVa = random.randint(1,5)
# print(skaiciukasVa)
# print(i)
#

# print('------------------------------1---------------------------------------')

# failas = open("naujasFailas.txt","r",encoding="utf8")
# print(failas.readlines())
# failas.close()

# failas = open("teksto_failas.txt", "a", encoding="utf8" )
# failas.write("Myliu saule, myliu lietu ir geles, vejas man ju milijona parnes\n")
# failas.close()
#
# failas = open("teksto_failas.txt", "r", encoding="utf8")
# print(failas.readlines())
# failas.close()
#
# failas = open("teksto_failas.txt", "r", encoding="utf8" )
# for line in failas.readlines():
#     print(line)
# failas.close()
#
# failas = open("teksto_failas.txt", "a", encoding="utf8")
# failas.write("saukia, iskeliauja pauksciai juokias, ruduo \n")
# failas.close()

# print('------------------------------2---------------------------------------')



# with open("antros_failas.txt", "w", encoding="utf8") as failas:
#     failas.write("Nauja eilute \n")
#     failas.write("Antra nauja eilute \n")
#
# with open("antros_failas2.txt", "w", encoding="utf8") as failas:
#     failas.write("Nauja eilute naujame faile \n")
#     failas.write("Antra nauja eilute antrame faile \n")
#
# with open("antros_failas.txt", "r") as failas:
#     print(failas.read())

# print('------------------------------3---------------------------------------')

failas = open("automobiliai.txt", "a", encoding="utf8" )
failas.write("  Marke    | Metai | Kaina    \n")
failas.write("   MB      | 2016  | 16000    \n")
failas.write("  BMW      | 2013  | 11000    \n")
failas.write("  BMW      | 2018  | 19000    \n")
failas.write("  Audi     | 2023  | 65000    \n")
failas.write("  Audi     | 2023  | 65000    \n")
failas.close()


with open("automobiliai.txt", "r") as failas:
    lines = failas.read().split("\n")
    for line in lines:
        cells = line.split("|")
        if len(cells) >= 2:
            metai = cells[1].strip()
            print(metai)

metai_suma = 0
automobiliu_kiekis = 0

with open("automobiliai.txt", "r") as failas:
    lines = failas.read().split("\n")
    for line in lines:
        cells = line.split("|")
        if len(cells) >= 2:
            try:
                metai = int(cells[1].strip())
                metai_suma += metai
                automobiliu_kiekis += 1
            except ValueError:
                print(f"Klaida skaitant metus eilutėje: {line.strip()}")

if automobiliu_kiekis > 0:
    metai_vidurkis = metai_suma / automobiliu_kiekis
    print(f"Automobilių metų vidurkis: {metai_vidurkis:.2f}")

    with open("rezultatai.txt", "w") as rezultatai_failas:
        rezultatai_failas.write(f"Automobilių metų vidurkis: {metai_vidurkis:.2f}\n")
else:
    print("Nėra duomenų apie automobilius.")
