import csv

file_path = r"C:\Users\Asus\Desktop\Business Intelligence\Python\sampleData.csv"

file = open(file_path, encoding="utf8")
file_read = csv.DictReader(file)


# print(----------------------------------1------------------------------------)
# kokios valiutos buvo naudotos?

unique_currencies = set()

with open("sampleData.csv", newline="", encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        currency = row[6]
        unique_currencies.add(currency)

print( "Naudotos valiutos:")
for currency in unique_currencies:
    print(currency)

# print(----------------------------------2------------------------------------)
# kiek income, outcome?(ignoruojant valiutas)
def calculate_income_and_outcome(file_path):
    income = 0
    outcome = 0

    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            suma = float(row["Suma"].replace(",", ""))
            dk = row["D/K"]

            if dk == "K":
                income += suma
            elif dk == "D":
                outcome += suma

    return income, outcome


total_income, total_outcome = calculate_income_and_outcome("sampleData.csv")
print("Total income and outcome:")
print("Income:", total_income)
print("Outcome:", total_outcome)




# def currency(file, colName):
#     curriencies = set()
#     for row in file:
#         currencies.add(row[colName])
#     return currencies
# currency = currency(file_read, colName="Valiuta")
# print(currency)

