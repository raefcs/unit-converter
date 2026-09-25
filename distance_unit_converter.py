



#units of conversion avaliable
avaliable_units = ["mm", "cm", "m", "ft", "yd", "mi", "mu", "km", 
"millimeters", "centimeters", "meters", "feet", "yards", "miles", 
"micrometers", "kilometers"] 

unit_1 = input( "Please eneter the unit of measurement you would like to convert (mm, cm, km, mi, etc): " )

#if unit not invalid

if unit_1  not in avaliable_units: 

	import sys

	sys.exit( "Error, Unit conversion not valid" )

#if unit valid

#initial distance
initial_dist = input( "Please enter disance in " + unit_1 + ": " )

#new unit conversion

unit_2 = input( "Please enter the unit you would like to convert " + initial_dist + " " + unit_1 + " to: ")

#if not valid

if unit_2 not in avaliable_units:
	
	import sys
	
	sys.exit( "Error, Unit conversion not valid" )
	
#if valid


#mm is initial unit


if unit_1 == "mm" or unit_1 == "millimeters":

#unit to meters

	unit_to_m = float(initial_dist) / 1000
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )



#cm is initial unit

		
if unit_1 == "cm" or unit_1 == "centimeters":

#unit to meters

	unit_to_m = float(initial_dist) / 100
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


#m is initial unit

		
if unit_1 == "m" or unit_1 == "meters":

#unit to meters

	unit_to_m = float(initial_dist)
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )






#ft is initial unit

		
if unit_1 == "ft" or unit_1 == "feet":

#unit to meters

	unit_to_m = float(initial_dist) / 3.281
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
		




#yd is initial unit

		
if unit_1 == "yd" or unit_1 == "yards":

#unit to meters

	unit_to_m = float(initial_dist) / 1.094
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )



#mi is initial unit

		
if unit_1 == "mi" or unit_1 == "miles":

#unit to meters

	unit_to_m = float(initial_dist) * 1609
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )






#mu is initial unit

		
if unit_1 == "mu" or unit_1 == "micrometers":

#unit to meters

	unit_to_m = float(initial_dist) / 1000000
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )







#km is initial unit

		
if unit_1 == "km" or unit_1 == "kilometers":

#unit to meters

	unit_to_m = float(initial_dist) * 1000
 
	if unit_2 == "m" or unit_2 == "meters":

		

		print( str(initial_dist) + " " + unit_1 + " = " + str(unit_to_m) + unit_2 )
		

	
	if unit_2 == "cm" or unit_2 == "centimeters":
	
		final_conv = round(unit_to_m * 100, 2)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	if unit_2 == "ft" or unit_2 == "feet":

		
		final_conv = (unit_to_m * 3.281)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
	

	if unit_2 == "yd" or unit_2 == "yards":


		final_conv = (unit_to_m * 1.094)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "mi" or unit_2 == "miles":


		final_conv = (unit_to_m / 1609)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )


		
	if unit_2 == "km" or unit_2 == "kilometers":


		final_conv = (unit_to_m / 1000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )

	
	if unit_2 == "micrometers" or unit_2 == "mu":


		final_conv = (unit_to_m * 1000000)
		
		print( str(initial_dist) + " " + unit_1 + " = " + str(final_conv) + unit_2 )
		
		


	
		



	