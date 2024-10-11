import datetime as dt

days_in_year = 360 # Just how escrow does it!
annual_tax = 0

annual_tax = float(input('Enter the annual property tax: '))
tax_per_day = annual_tax / days_in_year

print("The daily property tax is: $%0.2f" % tax_per_day)

# Get the closing date from user
date_entry = input("Enter the closing date in (MM-DD-YYYY Format): ")
closing_month, closing_day, closing_year = map(int, date_entry.split('-'))
closing_date = dt.date(closing_year, closing_month, closing_day)

# Using the closing date, determine if we're in the 1st installment period
# or the 2nd installment period
if(closing_date >= dt.date(closing_year,1,1)):
    delta_days = closing_date - dt.date(closing_year,1,1)
elif(closing_day >= dt.date(closing_year,7,1)):
    delta_days = closing_date - dt.date(closing_year,7,1)
    
print(f'Number of days from last installment date: {delta_days.days}')

seller_portion = delta_days.days * tax_per_day
buyer_portion = (annual_tax / 2) - seller_portion
print(f"Seller's tax responsibility: $%0.2f" % seller_portion)
print(f"Buyer's tax responsibility: $%0.2f" % buyer_portion)
