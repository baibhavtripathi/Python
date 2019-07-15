from datetime import date

#f_date= date (2018)

f_date = date(2018, 2, 11)
l_date = date(2018, 2, 16)

delta = l_date - f_date

print(delta.days)