import csv
from collections import defaultdict
import decimal

# Failas

file_path = r"C:\Users\Asus\Desktop\Business Intelligence\Python\sampleData.csv"

file = open(file_path, encoding="utf8")
file_read = csv.DictReader(file)


print('----------------------------------1------------------------------------')
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

print('----------------------------------2------------------------------------')
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

print('----------------------------------3------------------------------------')
# kiek income, outcome pagal kiekvieną valiutą?

# "Sąskaitos Nr.","","Data","Gavėjas","Paaiškinimai","Suma","Valiuta","D/K"
#
# unique_currencies = set()
# with open("sampleData.csv", newline="", encoding="utf8") as csvfile:
#     csv_reader = csv.reader(csvfile)
#     next(csv_reader)
#
#     for row in csv_reader:
#         currency = row[6]
#         unique_currencies.add(currency)
#
# print("Naudotos valiutos:")
# for currency in unique_currencies:
#     print(currency)

def calculate_income_and_outcome_by_currency(file_path):
    income_by_currency = {}
    outcome_by_currency = {}

    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            suma = float(row["Suma"].replace(",", ""))
            currency = row["Valiuta"]
            dk = row["D/K"]

            if currency not in income_by_currency:
                income_by_currency[currency] = 0
            if currency not in outcome_by_currency:
                outcome_by_currency[currency] = 0

            if dk == "K":
                income_by_currency[currency] += suma
            elif dk == "D":
                outcome_by_currency[currency] += suma

    return income_by_currency, outcome_by_currency

income_by_currency, outcome_by_currency = calculate_income_and_outcome_by_currency("sampleData.csv")

print("Total income by currency:")
for currency, income in income_by_currency.items():
    print(f"{currency}: {income:.2f}")

print("\nTotal outcome by currency:")
for currency, outcome in outcome_by_currency.items():
    print(f"{currency}: {outcome:.2f}")

print('--------------------------------4--------------------------------------')

# kiek buvo išleista kiekvieną mėnesį?

def calculate_outcome_by_month(file_path):
    outcome_by_month = {}

    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_date = row["Data"]
            month = full_date.split("-")[1]  # Išskaidykite datą ir paimkite tik mėnesio dalį
            expense = float(row["Suma"].replace(",", ""))
            dk = row["D/K"]

            if dk == "D":
                if month in outcome_by_month:
                    outcome_by_month[month] += expense
                else:
                    outcome_by_month[month] = expense

    return outcome_by_month

outcome_by_month = calculate_outcome_by_month("sampleData.csv")
print("Outcome by month:")
for month, outcome in outcome_by_month.items():
    print(f"Month: {month}, Total outcome: {outcome:.2f}")

print('--------------------------------5--------------------------------------')

# kiek buvo uždirbta kiekvieną mėnesį?

from collections import OrderedDict

def calculate_income_and_outcome_by_month(file_path):
    outcome_by_month = OrderedDict()

    def calculate_income_by_month(file_path):
        income_by_month = OrderedDict()

        with open(file_path, newline="", encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                full_date = row["Data"]
                date_parts = full_date.split("-")
                month = date_parts[1]  # Paimkite tik mėnesio dalį
                income = float(row["Suma"].replace(",", ""))
                if month in income_by_month:
                    income_by_month[month] += income
                else:
                    income_by_month[month] = income

        return income_by_month

    income_by_month = calculate_income_by_month(file_path)

    print("Income by month:")
    for month, income in income_by_month.items():
        print(f"Month: {month}, Total income: {income:.2f}")

    return outcome_by_month

outcome_by_month = calculate_income_and_outcome_by_month("sampleData.csv")

print('--------------------------------6--------------------------------------')

#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)


def calculate_balance_by_month(file_path):
    balance_by_month = defaultdict(float)
    current_balance = 0.00

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        sorted_rows = sorted(reader, key=lambda row: row["Data"])  # Surūšiuoti duomenis pagal datą

        for row in sorted_rows:
            if row["D/K"] == "D":  # Jei išlaidos, sumažinkite balansą
                current_balance -= float(row["Suma"].replace(",", ""))
            else:  # Jei pajamos, padidinkite balansą
                current_balance += float(row["Suma"].replace(",", ""))

            month = row["Data"].split("-")[1]  # Paimkite mėnesio dalį iš datos
            balance_by_month[month] = current_balance

    return balance_by_month

balance_by_month = calculate_balance_by_month("sampleData.csv")
print("Balance by month:")
for month, balance in balance_by_month.items():
    print(f"Month: {month}, Balance: {balance:.2f}")

print('--------------------------------7--------------------------------------')

#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?

def calculate_balance_by_currency_and_month(file_path):
    balance_by_currency_and_month = defaultdict(lambda: defaultdict(float))

    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_date = row["Data"]
            month = full_date.split("-")[1]
            currency = row["Valiuta"]
            amount = float(row["Suma"].replace(",", ""))

            if row["D/K"] == "D":
                balance_by_currency_and_month[currency][month] -= amount
            else:
                balance_by_currency_and_month[currency][month] += amount

    return balance_by_currency_and_month

def main():
    file_path = "sampleData.csv"
    balance_by_currency_and_month = calculate_balance_by_currency_and_month(file_path)

    print("Balance by currency and month:")
    for currency, month_balance in balance_by_currency_and_month.items():
        print(f"Currency: {currency}")
        for month, balance in month_balance.items():
            print(f"Month: {month}, Balance: {balance:.2f}")

if __name__ == "__main__":
    main()

print('--------------------------------8--------------------------------------')

# atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)
# -- sausis:
# -- -- income:
# -- -- Eur: 29%
# -- -- DK: 0%
# -- -- outcome:
# -- -- Eur: 36%
# -- -- DK: 19%

from collections import defaultdict

def calculate_income_and_outcome_by_month(file_path):
    income_by_month = defaultdict(float)
    outcome_by_month = defaultdict(float)
    total_income = 0
    total_outcome = 0

    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_date = row["Data"]
            month = full_date.split("-")[1]
            currency = row["Valiuta"]
            amount = float(row["Suma"].replace(",", ""))

            if row["D/K"] == "D":
                outcome_by_month[month] += amount
                total_outcome += amount
            else:
                income_by_month[month] += amount
                total_income += amount

    return income_by_month, outcome_by_month, total_income, total_outcome

def calculate_percentage(income, outcome, total_income, total_outcome):
    income_percentage = {month: (income[month] / total_income) * 100 for month in income}
    outcome_percentage = {month: (outcome[month] / total_outcome) * 100 for month in outcome}
    return income_percentage, outcome_percentage

def main():
    file_path = "sampleData.csv"
    income_by_month, outcome_by_month, total_income, total_outcome = calculate_income_and_outcome_by_month(file_path)
    income_percentage, outcome_percentage = calculate_percentage(income_by_month, outcome_by_month, total_income, total_outcome)

    months = sorted(set(income_by_month.keys()) | set(outcome_by_month.keys()))
    for month in months:
        print(f"-- {month}:")
        print(f"-- -- income:")
        for currency, percentage in income_percentage.items():
            print(f"-- -- {currency}: {percentage:.0f}%")
        print(f"-- -- outcome:")
        for currency, percentage in outcome_percentage.items():
            print(f"-- -- {currency}: {percentage:.0f}%")

if __name__ == "__main__":
    main()


