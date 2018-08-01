# Calculate the total pay while taking into account
# possible overtime for any hours over 40

hrs = raw_input("Enter Hours:")
rt = raw_input("Enter Rate:")

h = float(hrs)
r = float(rt)

if h <= 40:
    pay = h * r
else :
    pay = r * 40 + ((r * 1.5) *(h - 40))

print pay             
