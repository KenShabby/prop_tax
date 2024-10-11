'''
A simple program to calculate the property tax prorations for a given closing 
date.  Based on a 360 day year, with the 1st installment running from July 1
to December 30, and the 2nd installment from January 1st to June 30th.
'''

import datetime as dt

days_in_year = 360 # Just how escrow does it!
annual_tax = 0

# Todo: clean input
annual_tax = float(input('Enter the annual property tax: '))
tax_per_day = annual_tax / days_in_year

print("The daily property tax is: $%0.2f" % tax_per_day)

# Get the closing date from user
# Todo: check for proper input, handle exceptions
date_entry = input("Enter the closing date in (MM-DD-YYYY Format): ")
closing_month, closing_day, closing_year = map(int, date_entry.split('-'))
closing_date = dt.date(closing_year, closing_month, closing_day)

# Using the closing date, determine if we're in the 1st installment period
# or the 2nd installment period
# Todo: Handle out of range dates
if(closing_date >= dt.date(closing_year,1,1)):
    delta_days = closing_date - dt.date(closing_year,1,1)
elif(closing_day >= dt.date(closing_year,7,1)):
    delta_days = closing_date - dt.date(closing_year,7,1)
    
print(f'Number of days from last installment date: {delta_days.days}')

seller_portion = delta_days.days * tax_per_day
buyer_portion = (annual_tax / 2) - seller_portion
print(f"Seller's tax responsibility: $%0.2f" % seller_portion)
print(f"Buyer's tax responsibility: $%0.2f" % buyer_portion)
