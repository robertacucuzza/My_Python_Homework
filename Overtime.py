hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate:")
r = float(rate)
overtime=(r*1.5)
if h < 40:
    print(h*r)
else:
	print(((h-40)*overtime)+(40*r))
