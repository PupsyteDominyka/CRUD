# failas = open("naujasFailas.txt","a",encoding="utf8")
# print(failas.write("ožėlis mažasis\n"))
# failas.close()
import random
import  csv

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
#
# failas = open("automobiliai.txt", "a", encoding="utf8" )
# failas.write("  Marke    | Metai | Kaina    \n")
# failas.write("   MB      | 2016  | 16000    \n")
# failas.write("  BMW      | 2013  | 11000    \n")
# failas.write("  BMW      | 2018  | 19000    \n")
# failas.write("  Audi     | 2023  | 65000    \n")
# failas.write("  Audi     | 2023  | 65000    \n")
# failas.close()
#
#
# with open("automobiliai.txt", "r") as failas:
#     lines = failas.read().split("\n")
#     for line in lines:
#         cells = line.split("|")
#         if len(cells) >= 2:
#             metai = cells[1].strip()
#             print(metai)
#
# metai_suma = 0
# automobiliu_kiekis = 0
#
# with open("automobiliai.txt", "r") as failas:
#     lines = failas.read().split("\n")
#     for line in lines:
#         cells = line.split("|")
#         if len(cells) >= 2:
#             try:
#                 metai = int(cells[1].strip())
#                 metai_suma += metai
#                 automobiliu_kiekis += 1
#             except ValueError:
#                 print(f"Klaida skaitant metus eilutėje: {line.strip()}")
#
# if automobiliu_kiekis > 0:
#     metai_vidurkis = metai_suma / automobiliu_kiekis
#     print(f"Automobilių metų vidurkis: {metai_vidurkis:.2f}")
#
#     with open("rezultatai.txt", "w") as rezultatai_failas:
#         rezultatai_failas.write(f"Automobilių metų vidurkis: {metai_vidurkis:.2f}\n")
# else:
#     print("Nėra duomenų apie automobilius.")

# print('------------------------------4---------------------------------------')

#
# with open("studentai.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["vardas", "pavarde", "amzius", "pazymiai"])
#     writer.writerow(["Jonas", "Jonauskas", 20, "8 9 7 10 6"])
#     writer.writerow(["Petras", "Petrauskas", 21, "9 8 7 6 5"])
#     writer.writerow(["Ona", "Onute", 19, "10 9 10 8 7"])
#
# print("Nuskaitymas su csv.reader:")
# with open("studentai.csv", newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # Praleidžiame antraštę
#     for row in reader:
#         print(row)
#
# print("\nNuskaitymas su csv.DictReader:")
# with open("studentai.csv", newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
#
# # print('------------------------------5---------------------------------------')
#
# with open("prekes.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["prekes_kodas", "pavadinimas", "kaina", "kiekis"])
#     writer.writerow(["1234", "Lempa", 15.99, 10])
#     writer.writerow(["5678", "Stalas", 99.99, 5])
#     writer.writerow(["91011", "Kėdė", 49.99, 8])
#
# print("Nuskaitymas su csv.reader:")
# with open("prekes.csv", newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # Praleidžiame antraštę
#     for row in reader:
#         print(row)
# print("\nNuskaitymas su csv.DictReader:")
# with open("prekes.csv", newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)

# print('------------------------------6---------------------------------------')
#
# with open("studentai.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["vardas", "pavarde", "amzius", "pazymiai"])
#     writer.writerow(["Jonas", "Jonauskas", 20, "8 9 7 10 6"])
#     writer.writerow(["Petras", "Petrauskas", 21, "9 8 7 6 5"])
#     writer.writerow(["Ona", "Onute", 19, "10 9 10 8 7"])
#
# with open("studentai.csv", newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     studentai = list(reader)
#
# geriausias_studentas = max(studentai, key=lambda x: sum(map(int, x["pazymiai"].split())))
# print("Geriausiai besimokantis studentas:", geriausias_studentas)
#
# vyriausias_studentas = max(studentai, key=lambda x: int(x["amzius"]))
# print("Vyriausias studentas:", vyriausias_studentas)
#
# mažiausias_vidurkis = min(studentai, key=lambda x: sum(map(int, x["pazymiai"].split())))
# print("Mažiausias vidurkis:", mažiausias_vidurkis)
#
# with open("rezultatai.txt", "w") as rezultatai_failas:
#     rezultatai_failas.write("Geriausiai besimokantis studentas: " + str(geriausias_studentas) + "\n")
#     rezultatai_failas.write("Vyriausias studentas: " + str(vyriausias_studentas) + "\n")
#     rezultatai_failas.write("Mažiausias vidurkis: " + str(mažiausias_vidurkis) + "\n")

# print('------------------------------7---------------------------------------')
#
# with open("studentai.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Vardas", "Pavarde", "Amzius", "Pazymiai"])
#     writer.writerow(["Jonas", "Jonaitis", 20, "8 9 7 10 6"])
#     writer.writerow(["Petras", "Petraitis", 21, "9 8 7 6 5"])
#     writer.writerow(["Ona", "Onaite", 19, "10 9 10 8 7"])
#     writer.writerow(["Maryte", "Marytite", 22, "6 7 8 9 10"])
#
# with open("studentai.csv", newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     studentai = list(reader)
#
# filtruoti_studentai = [studentas for studentas in studentai if sum(map(int, studentas["Pazymiai"].split())) / len(studentas["Pazymiai"].split()) > 8]
#
# with open("atfiltruoti_studentai.csv", "w", newline='') as csvfile:
#     fieldnames = ["Vardas", "Pavarde", "Amzius", "Pazymiai"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for studentas in filtruoti_studentai:
#         writer.writerow(studentas)
#
# print("Duomenys atfiltruoti ir išsaugoti į atfiltruoti_studentai.csv failą.")













