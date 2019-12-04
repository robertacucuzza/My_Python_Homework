hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h=float(hrs)
r=float(rate)
overtime=(r*1.5)
def computepay(h,r):
    if h<40:
    	return(h*r)
    else:
        return(((h-40)*overtime)+(40*r))

p = computepay(h,r)
print(p)
#this us a change
