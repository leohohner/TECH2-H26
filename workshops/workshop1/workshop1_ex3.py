import numpy as np 
def taxes(income):
    """
    Return the taxes owed for a given income.

    Parameters
    ----------
    income
        Gross income

    Returns
    -------
    Tax owed
    """
    if income <= 300_000:
        print(f'You dont have to pay any taxes.')
    elif 300_000 < income <= 700_000:
        taxes = (income - 300_000) * 0.2
    else:
        taxes = 0.35 * (income - 700_000) + 0.2 * (400_000)

    return taxes

#Create 13 candiadate income levels for testing
income = np.linspace(0,1_200_000, 13)

taxes_loop = []

for income in incomes:
    #Compute taxes for current income level
    taxes = tax(income)  # noqa: F811
    #Append to list 
    taxes_loop.append(taxes)
    #Income after tax
    net_income = income - taxes

print(f"Gross income: {income:10.0f};"
    f"Taxes: {taxes:10.0f};"
    f"Net income {net_income:10.0f}"
    )



#print(f'You owe {tax(1000000)} Nok in Taxes.')
