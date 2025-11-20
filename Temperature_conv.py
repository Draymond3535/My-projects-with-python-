
print('Welcome to my private sector , where all your dreams come true ')
print('Choose what you want to convert :')
print( '1.Convert Celsius to Kelvin')
print ('or')
print('2.Convert  Kelvin to Celsus ')
user = int(input("1 or 2 : "))
if user == 1: 
   c= float(input('What is the temperature in Celsus: '))
   total= c +  273.15
   print('The temperature in kelvin is ',total,'K')
elif user ==2 :
  d= float(input('What is temperature in kelvin : '))
  total_2= d - 273.15
  print('The temperature in Celsus is :',total_2, 'C')
print ('Thank you for your participation !')

