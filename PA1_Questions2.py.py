#Python Script to convert units from US imperial to international metric

print ("Welcome to the Python Unit Converter!")
print ("This converter can convert from gal, lb and mi")
print ("This converter can convert to l, kg and km")
print ("Note that this converter will only work with compatible units")

#The above statements give the instructions for the program and also the rules

print ("Unit Conversion") 

start = raw_input("Convert from? (only gal, lb and mi)")
end = raw_input ("Convert to? (only l, kg and km)")

#The above two variables are defined for the input and the output units.

if start == "gal" and end == "l": #Checks whether the units match
    value = input ("Value?")
    print str(value)+str(start), ("="), str(value*3.7541), str(end)

elif start == "lb" and end == "kg": #Checks whether the units match
    value = input ("Value?")
    print str(value)+str(start), ("="), str(value*0.45359), str(end)

elif start == "mi" and end == "km": #Checks whether the units match
    value = input ("Value?")
    print str (value)+str(start), ("="), str(value*1.60934), str(end)

#Printed when the units to be converted do not match
else: 
    print ("Error: Incompatible Conversion!")
    print ("Please select the correct units for conversion")
    
