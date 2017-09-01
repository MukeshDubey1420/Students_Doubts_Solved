def KelvinToFahrenheit(Temperature):
   assert (Temperature == 0)," absolute zero!"
   return ((Temperature-273)*1.8)+32
a=int(raw_input('enter tmap'))
print KelvinToFahrenheit(a)