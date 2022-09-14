import math
x= -4.5
y= 0.75**-4
z= -0.845**2
s=((math.pow((9 + (x-y)**2),1/3))/(x**2+y**2+2)) - (math.pow(math.e, math.fabs(x-y))*math.pow(math.tan(z), 3))

print("s = {0: .5f}".format(s))
