# Implimenting the 'try / except' function for the first time

usrinput = raw_input("Enter Number")

try:
    numinput = float(usrinput)
except:
    numinput = -1
    print "Please Enter a Number"

if numinput >= 0.9:
    print "A"
elif numinput >= 0.8:
    print "B"
elif numinput >= 0.7:
    print "C"
elif numinput >= 0.6:
    print "D"
else:
    print "F"
