from datetime import date
a = date.today()
b = int(input("Enter a finishing Year"))
for yr in range(a.year, b):
   if (0 == yr % 4) and (0 != yr % 100) or (0 == yr % 400):
       print(yr)
