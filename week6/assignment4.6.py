def computepay(h,r):
   
    if(h<40):
        pay = h*r
    else:
        pay = r*40+(h-40)*r*1.5
    return pay

hrs = input("Enter Hours:")
rate = input("Rate per Hour:")

try: 
    h = float(hrs)
    r = float(rate)
except:
    print("Enter Numeric Values")
    quit()


p = computepay(h,r)
print(p)
