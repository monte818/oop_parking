def rentalCalc():
    rental_income = 0
    expenses = 0

    while True:
        rental_inp = float(input("What is your monthly rental income including rental, laundry storage, and other forms of income from the property? "))
        tax_inp = float(input("Now time for expenses, what is the tax for your property? "))
        ins_inp = float(input("How much is the insurance on the property? "))
        mortg_ask = 0

        cash_purchase = input("Do you have a mortgage on the property? (Enter 'yes' or 'no'): ").lower() == 'no'
        if not cash_purchase:
            mortg_ask = float(input("How much is the mortgage on the property? "))

        owner_pays_util = input("Does the tenant pay for utilities? (Enter 'yes' or 'no'): ").lower() == 'no'

        utility_cost = 0
        if owner_pays_util:
            utility_cost = float(input("How much are the monthly utility costs paid by the landlord? "))

        owner_pays_hoa = input("Does the renter pay for HOA fees? (Enter 'yes' or 'no'): ").lower() == 'yes'

        hoa_fee = 0
        if not owner_pays_hoa:
            hoa_inp = input("How much are the HOA fees? If there are none, type [N]: ")
            if hoa_inp.lower() != "n":
                hoa_fee = float(hoa_inp)

        misc_expenses = float(input("Enter any other miscellaneous monthly expenses: "))

        total_expenses = tax_inp + ins_inp + mortg_ask + hoa_fee + utility_cost + misc_expenses
        expenses += total_expenses
        rental_income = rental_inp - total_expenses

        annual_income = rental_income * 12
        print(f"Total Monthly Expenses: {total_expenses}")
        print(f"Rental Income Cash Flow: {rental_income}")
        print(f"The annual cash flow is {annual_income}")

        down_close = float(input("What were your down payments and closing with rehab your full out of pocket cash down written here: "))

        cash_oncash = annual_income / down_close
        cash_percent = round(cash_oncash * 100)
        print(f"Cash on Cash ROI percentage is: {cash_percent}%")

        choice = input("Do you want to calculate for another property? (Enter 'yes' to continue or any other key to exit): ")
        if choice.lower() != 'yes':
            break

    print(f"Total Monthly Expenses for all properties: {expenses}")

rentalCalc()