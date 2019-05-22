hrs = input("Enter Hours:")
rate = input("Rate per hours:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter Numeric Input")
    quit()    

if h<=40:
    answer=r*h
else:
	answer=(r*40)+(1.5*(h-40)*r)
    
print(answer)
