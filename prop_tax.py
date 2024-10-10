import datetime as dt

days_in_year = 360 # Just how escrow does it!
annual_tax = 0

annual_tax = float(input('Enter the annual property tax: '))

tax_per_day = annual_tax / days_in_year

print("The daily property tax is: $%0.2f" % tax_per_day)

# print('Enter the closing date: ', end='')
closing_date = dt.date(2024, 10, 3) 
print(f'Closing date: {closing_date}')

delta_days = closing_date - dt.date(2024,7,1)
print(f'Number of days from last installment date: {delta_days.days}')

seller_portion = delta_days.days * tax_per_day
buyer_portion = (annual_tax / 2) - seller_portion
print(f"Seller's tax responsibility: $%0.2f" % seller_portion)
print(f"Buyer's tax responsibility: $%0.2f" % buyer_portion)


# calculate the number of days from the closing date to previous installment date

# The 1st installment period runs from July 1st to January 1st. The payment for
# this period is due on November 1st and is delinquent and subject  to penalty
# after December 10th.

# The 2nd installment period runs from January 1st to July 1st. The payment for
# this period is due on February  1st and delinquent and subject to penalty
# after April 10th.
