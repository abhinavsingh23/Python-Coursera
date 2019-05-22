hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Rate per hours:")
r = float(rate)

if h<=40:
    answer=r*h
else:
	answer=(r*40)+(1.5*(h-40)*r)
    
print(answer)
