import math
radius=input("Verdien til radius?\n>")
radius=float(radius)

diameter= 2*radius
areal=math.pi*radius*radius
omkrets=2*math.pi*radius

print("\nDiameter: {0: .2f}".format(diameter))
print("Areal:   {0: .2f}".format(areal))
print("Omkrets:  {0: .2f}".format(omkrets))
