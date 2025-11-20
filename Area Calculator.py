import math 
print("Area Calculator 📐")
print("1) Triangle")
print("2) Rectangle") 
print("3) Square")
print("4) Circle")
print("5)Quit")
fig= int(input("Which Shape:"))
a=1
b=2
c=3
d=4
e=5
if fig==a :
  ba= float(input("Base:"))
  he= float(input("Height:"))
  area= (ba*he)/2
  print("The area of the triangle is", area)
elif fig ==b :
  le= float(input("Length:"))
  wi= float(input("Width:"))
  area_2= le*wi
  print("The area of the rectangle is", area_2)
elif  fig == c :
  co= float(input("Side :"))
  area_3= co**2
  print("The area of the square is ", area_3)
elif fig == d:
  ra= float(input("Radius:"))
  area_4= math.pi * (ra**2)
  print("The area of the circle is ",area_4,)
elif fig == e:
  print("Good bye !")
else :
  print("Error . Please try again.")