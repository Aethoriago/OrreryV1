###
# https://en.wikipedia.org/wiki/Best_coding_practices
#
#https://github.com/Aethoriago/OrreryV1/blob/master/README.md
#Notes:
#https://eyes.nasa.gov/apps/orrery/
#https://ssd.jpl.nasa.gov/?email_list
#https://solarsystem.nasa.gov/overlay-orrery/
#https://www.epochconverter.com/
#https://en.wikipedia.org/wiki/Eccentricity_(mathematics)
#    [https://www.princeton.edu/~willman/planetary_systems/Sol/]
#https://technology.nasa.gov/patent/NPO-TOPS-26
#
###

import time

p_dict = {
    #'Planet' : [SmA, Ecc, OP, Me],
    'Mercury': [0,0.3870993, 0.20564, 0.2408467, 0.05527],
    'Venus' : [0,0.023336, 0.00678, 0.61519726, 0.81500],
    'Earth' : [0,1.000003, 0.01671, 1.0000174, 1.0000],
    'Mars' : [0,1.52371, 0.09339, 1.8808158, 0.10745],
    'Jupiter' : [0,5.2029, 0.0484, 11.862615, 317.83],
    'Saturn' : [0,9.537, 0.0539, 29.447498, 95.159],
    'Uranus' : [0,19.189, 0.04726, 84.016846, 14.5],
    'Neptune' : [0,30.0699, 0.00859, 164.79132, 17.204],
    'Ceres' : [0,2.7658, 0.078, 4.59984, 0.00016],
    'Pluto' : [0,39.4821, 0.24883, 248.0208, 0.00220],
    'Haumea' : [0,43.34, 0.189, 285.4, 0.00070],
    'Makemake' : [0,45.79, 0.159, 309.9, 0.0007],
    'Eris' : [0,67.67, 0.44177, 557.2, 0.00278]
}

Ex = 1

AU = 149597870700
Yr = 365.25
YrS = 31557600
Me = 5974200000000000000000000
    #Note that Me is Mass relative to Earth Mass I.E 1Me = same mass as Earth. The string output is the actual mass however.
Epoch = time.gmtime(time.time())


Planets = "| SemimajorAxis: %r AU | Eccentricity: %r | Orbital Period: %r Years(%r Years in Seconds) | Mass(kg): %r |"



print("Planets")
print("")

print("Mercury:")
print(Planets % (p_dict['Mercury'][1],p_dict['Mercury'][2],p_dict['Mercury'][3],(p_dict['Mercury'][3]*YrS),(p_dict['Mercury'][4]*Me)))
print("")

print("Venus:")
print(Planets % (p_dict['Venus'][1],p_dict['Venus'][2],p_dict['Venus'][3],(p_dict['Venus'][3]*YrS),(p_dict['Venus'][4]*Me)))
print("")

print("Earth:")
print(Planets % (p_dict['Earth'][1],p_dict['Earth'][2]],p_dict['Earth'][3],(p_dict['Earth'][3]*YrS),(p_dict['Earth'][4]*Me)))
print("")

print("Mars")
print(Planets % (p_dict['Mars'][1],p_dict['Mars'][2],p_dict['Mars'][3],(p_dict['Mars'][3]*YrS),(p_dict['Mars'][4]*Me)))
print("")

print("Jupiter:")
print(Planets % (p_dict['Jupiter'][1],p_dict['Jupiter'][2],p_dict['Jupiter'][3],(p_dict['Jupiter'][3]*YrS),(p_dict['Jupiter'][4]*Me)))
print("")

print("Saturn:")
print(Planets % (p_dict['Saturn'][1],p_dict['Saturn'][2],p_dict['Saturn'][3],(p_dict['Saturn'][3]*YrS),(p_dict['Saturn'][4]*Me)))
print("")

print("Uranus:")
print(Planets % (p_dict['Uranus'][1],p_dict['Uranus'][2],p_dict['Uranus'][3],(p_dict['Uranus'][3]*YrS),(p_dict['Uranus'][4]*Me)))
print("")

print("Neptune:")
print(Planets % (p_dict['Neptune'][1],p_dict['Neptune'][2],p_dict['Neptune'][3],(p_dict['Neptune'][3]*YrS),(p_dict['Neptune'][4]*Me)))
print("")

print("Dwarf Planets")
print("")

print("Ceres:")
print(Planets % (p_dict['Ceres'][1],p_dict['Ceres'][2],p_dict['Ceres'][3],(p_dict['Ceres'][3]*YrS),(p_dict['Ceres'][4]*Me)))

print("Plutoids")
print("")

print("Pluto")
print(Planets % (p_dict['Pluto'][1],p_dict['Pluto'][2],p_dict['Pluto'][3],(p_dict['Pluto'][3]*YrS),(p_dict['Pluto'][4]*Me)))
print("")

print("Haumea")
print(Planets % (p_dict['Haumea'][1],p_dict['Haumea'][2],p_dict['Haumea'][3],(p_dict['Haumea'][3]*YrS),(p_dict['Haumea'][4]*Me)))
print("")

print("Makemake")
print(Planets % (p_dict['Makemake'][1],p_dict['Makemake'][2],p_dict['Makemake'][3],(p_dict['Makemake'][3]*YrS),(p_dict['Makemake'][4]*Me)))
print("")

print("Eris")
print(Planets % (p_dict['Eris'][1],p_dict['Eris'][2],p_dict['Eris'][3],(p_dict['Eris'][3]*YrS),(p_dict['Eris'][4]*Me)))
print("")

#wait function
input()