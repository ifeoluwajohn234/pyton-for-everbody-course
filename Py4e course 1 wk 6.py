def computepay(h, r):
    if h > 40.0:
        initial_pay = r * h
        additional_pay = (h-40.0)*(r*0.5)
        p = initial_pay + additional_pay
    else:
        p = r *h
    return p
    

h = input("Enter Hours:")
r = input('Enter Rate:')
p = computepay(float(h),float (r))
print("Pay", p)