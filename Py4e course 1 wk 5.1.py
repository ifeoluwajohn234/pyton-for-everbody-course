hrs = input("Enter Hours:")
rates = input('Enter Rate:')
try:
    r = float(rates)
    h = float(hrs)
except:
    print("errror in value entered try numbers only")
    quit()
#r = float(rates)
#h = float(hrs)
if h > 40.0 :
    initial_pay = r * h
    additional_pay = (h-40.0)*(r*0.5)
    pay = initial_pay + additional_pay
else:
    pay = r *h
print(pay)