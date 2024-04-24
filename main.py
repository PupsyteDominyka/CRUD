# failas = open("naujasFailas.txt","a",encoding="utf8")
# print(failas.write("ožėlis mažasis\n"))
# failas.close()
import random

failas = open("naujasFailas.txt","r",encoding="utf8")
print(failas.readlines())
failas.close()

failas = open("naujasFailas.txt","r",encoding="utf8")
for line in failas.readlines():
    print(line)
failas.close()


with open("naujasFailas.txt", "r",encoding="utf8") as failas:
    lines = failas.read().split("\n")
    for line in lines:
        print(line)



def formatName(name):
    res = ""
    for part in name.split(" "):
        res += str(part[0]).upper() + str(part[1:]).lower() + " "
    return res[:-1]

print(formatName("naglis jonas"))
print(formatName("Naglis jonas"))
print(formatName("nAGLIS jONAS"))



text = "labas rytas grazus oras"
print(text)
print(text.split("s"))
for txt in text.split("s"):
    if txt != "":
        print("|" + txt + "|")

for i in range(1):
    skaiciukasVa = random.randint(1,5)
print(skaiciukasVa)
print(i)