import csv
from collections import OrderedDict
from collections import defaultdict

def get_unique_currencies(file_path):
    unique_currencies = set()
    with open(file_path, newline="", encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            currency = row[6]
            unique_currencies.add(currency)
    return unique_currencies

def main():
    file_path = "sampleData.csv"
    currencies = get_unique_currencies(file_path)
    print("Naudotos valiutos:")
    for currency in currencies:
        print(currency)
if __name__ == "__main__":
    main()

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
def main():
    total_income, total_outcome = calculate_income_and_outcome("sampleData.csv")
    print("Total income and outcome:")
    print("Income:", total_income)
    print("Outcome:", total_outcome)
if __name__ == "__main__":
    main()

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


def main():
    file_path = "sampleData.csv"
    unique_currencies = get_unique_currencies(file_path)
    print("Naudotos valiutos:")
    for currency in unique_currencies:
        print(currency)
    income_by_currency, outcome_by_currency = calculate_income_and_outcome_by_currency(file_path)
    print("\nTotal income by currency:")
    for currency, income in income_by_currency.items():
        print(f"{currency}: {income:.2f}")
    print("\nTotal outcome by currency:")
    for currency, outcome in outcome_by_currency.items():
        print(f"{currency}: {outcome:.2f}")
if __name__ == "__main__":
    main()

def calculate_income_and_outcome_by_month(file_path):
    income_by_month = OrderedDict()
    outcome_by_month = OrderedDict()
    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_date = row["Data"]
            date_parts = full_date.split("-")
            month = date_parts[1]  # Paimkite tik mėnesio dalį
            income = float(row["Suma"].replace(",", ""))
            dk = row["D/K"]
            if dk == "K":
                if month in income_by_month:
                    income_by_month[month] += income
                else:
                    income_by_month[month] = income
            elif dk == "D":
                if month in outcome_by_month:
                    outcome_by_month[month] += income
                else:
                    outcome_by_month[month] = income
    print("Income by month:")
    for month, income in income_by_month.items():
        print(f"Month: {month}, Total income: {income:.2f}")
    print("\nOutcome by month:")
    for month, outcome in outcome_by_month.items():
        print(f"Month: {month}, Total outcome: {outcome:.2f}")
    return outcome_by_month
outcome_by_month = calculate_income_and_outcome_by_month("sampleData.csv")

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
    balance_by_currency_and_month = calculate_balance_by_currency_and_month("sampleData.csv")
    print("Balance by currency and month:")
    for currency, month_balance in balance_by_currency_and_month.items():
        print(f"Currency: {currency}")
        for month, balance in month_balance.items():
            print(f"Month: {month}, Balance: {balance:.2f}")
if __name__ == "__main__":
    main()


def calculate_income_and_outcome_by_month(file_path):
    income_by_month = defaultdict(lambda: defaultdict(float))
    outcome_by_month = defaultdict(lambda: defaultdict(float))
    total_income = defaultdict(float)
    total_outcome = defaultdict(float)
    with open(file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_date = row["Data"]
            month = full_date.split("-")[1]
            currency = row["Valiuta"]
            amount = float(row["Suma"].replace(",", ""))
            dk = row["D/K"]
            if dk == "K":
                income_by_month[month][currency] += amount
                total_income[currency] += amount
            elif dk == "D":
                outcome_by_month[month][currency] += amount
                total_outcome[currency] += amount
    return income_by_month, outcome_by_month, total_income, total_outcome

def calculate_percentage(income, outcome, total_income, total_outcome):
    income_percentage = {}
    outcome_percentage = {}
    for month in income:
        income_percentage[month] = {}
        for currency in income[month]:
            income_percentage[month][currency] = (income[month][currency] / total_income[currency]) * 100
        outcome_percentage[month] = {}
        for currency in outcome[month]:
            outcome_percentage[month][currency] = (outcome[month][currency] / total_outcome[currency]) * 100
    return income_percentage, outcome_percentage

def main():
    file_path = "sampleData.csv"
    income_by_month, outcome_by_month, total_income, total_outcome = calculate_income_and_outcome_by_month(file_path)
    income_percentage, outcome_percentage = calculate_percentage(income_by_month, outcome_by_month, total_income,
                                                                 total_outcome)
    months = sorted(set(income_by_month.keys()) | set(outcome_by_month.keys()))
    for month in months:
        print(f"-- {month}:")
        if month in income_by_month:
            print(f"-- -- income:")
            for currency, percentage in income_percentage[month].items():
                print(f"-- -- {currency}: {percentage:.0f}%")
        if month in outcome_by_month:
            print(f"-- -- outcome:")
            for currency, percentage in outcome_percentage[month].items():
                print(f"-- -- {currency}: {percentage:.0f}%")

if __name__ == "__main__":
    main()






