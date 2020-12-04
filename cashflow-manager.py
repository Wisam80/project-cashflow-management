# Management System APP
# user_name=(input("What is your name? "))
# 1. Income:
income = {}
name_of_income = []
amount_of_income = []
total_income = 0

# 2. Expenditures:
expenditures = {}
name_of_expenditures = []
amount_of_expenditures = []
total_expenditures = 0

# balance
remaining_balance = 0

management_system = (
    input("What information do you want to enter? \nPress: \n(i) for income, \n(e) for expenditure,"
          "\n(c) for current balance,\n(s) for summary or\n(q) to quit.\n"))
while len(management_system) > 0 and not (management_system == "q" or management_system == "Q"):
    if management_system == "i" or management_system == "I":
        income_name = (input("Enter the NAME of your income: "))
        name_of_income.append(income_name)
        lenght = len(name_of_income)
        income_amount = int(input("Enter the AMOUNT of this income: "))
        amount_of_income.append(income_amount)
        total_income = sum(amount_of_income)

    if management_system == "e" or management_system == "E":
        expenditure_name = (input("Enter the NAME of your expenditure: "))
        name_of_expenditures.append(expenditure_name)
        lenght = len(name_of_expenditures)
        expenditure_amount = int(input("Enter the AMOUNT of this expenditure: "))
        amount_of_expenditures.append(expenditure_amount)
        total_expenditures = sum(amount_of_expenditures)
        # 3. Warning if total expenditures are higher than total income:
        if total_expenditures > total_income:
            print("!!! WARNING!!! YOUR EXPENDITURES ARE HIGHER THAN YOUR INCOME!!! \n\n")

    if management_system == "c" or management_system == "C":
        remaining_balance = (total_income - total_expenditures)
        print("your remaining balance is: ", remaining_balance, "\n\n")

    if management_system == "s" or management_system == "S":
        income = zip(name_of_income, amount_of_income)
        income_dict = dict(income)
        print("total income per month: ", total_income)
        print("income per month", income_dict, "\n\n")

        expenditures = zip(name_of_expenditures, amount_of_expenditures)
        expenditures_dict = dict(expenditures)

        print("total expenditures per month: ", total_expenditures)
        print("expenditures per month", expenditures_dict, "\n\n")

        if total_income > 0:
            # 4. Percent Expenditure of total income:
            percent_expenditure = total_expenditures * 100 / total_income
            print("your expenditures in percent is: ", percent_expenditure, "\n\n")
            # 5. Percent balance of total income:
            percent_balance = remaining_balance * 100 / total_income
            print("your remaining balance in percent is: ", percent_balance, "\n\n")

        if expenditures_dict and amount_of_expenditures:
            # 6. max. single expenditure:
            print("the highest single expenditure is: ", max(expenditures_dict), ": ", max(amount_of_expenditures))

        if income_dict and amount_of_income:
            # 7. max. single income:
            print("the highest single income is: ", max(income_dict), ": ", max(amount_of_income))

    management_system = input("Do you want to enter more information?"
                              "\nPress (i) for income, \n(e) for expenditure,"
                              "\n(c) for current balance,\n(s) for summary\nor (q) to quit.\n")
