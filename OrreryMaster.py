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
    #'Planet' : [SmA, Ecc, OP, Me, PH, AH],
    'Mercury': [0,      0.3870993, 0.20564, 0.2408467, 0.05527, 46001009, 69817445],
    'Venus' : [0,       0.023336, 0.00678, 0.61519726, 0.81500, 107476170, 108942780],
    'Earth' : [0,       1.000003, 0.01671, 1.0000174, 1.0000, 147098291, 152098233],
    'Mars' : [0,        1.52371, 0.09339, 1.8808158, 0.10745, 206655215, 249232432], # note that Ceres is between Mars and Jupiter
    'Jupiter' : [0,     5.2029, 0.0484, 11.862615, 317.83, 740679835, 816001807],
    'Saturn' : [0,      9.537, 0.0539, 29.447498, 95.159, 1349823615, 1503509229],
    'Uranus' : [0,      19.189, 0.04726, 84.016846, 14.5, 2734998229, 3006318143],
    'Neptune' : [0,     30.0699, 0.00859, 164.79132, 17.204, 4459753056, 4537039826],
    'Ceres' : [0,       2.7658, 0.078, 4.59984, 0.00016, 380951528, 446428973],
    'Pluto' : [0,       39.4821, 0.24883, 248.0208, 0.00220, 4436756954, 7376124302],
    'Haumea' : [0,      43.34, 0.189, 285.4, 0.00070, 5157623774, 7706399149],
    'Makemake' : [0,    45.79, 0.159, 309.9, 0.0007, 5671928586, 7894762625],
    'Eris' : [0,        67.67, 0.44177, 557.2, 0.00278, 576732799, 14594512904]
}



AU = 149597870700
Yr = 365.25
YrS = 31557600
Me = 5974200000000000000000000
    #Note that Me is Mass relative to Earth Mass I.E 1Me = same mass as Earth. The string output is the actual mass however.
Epoch = time.gmtime(time.time())


Planets = "| SemimajorAxis: %r AU | Eccentricity: %r | Orbital Period: %r Years(%r Years in Seconds) | Mass(kg): %r | Perihelion (km) %r | Aphelion (km) %r |"



print("Planets")
print("")

print("Mercury:")
print(Planets % (p_dict['Mercury'][1],p_dict['Mercury'][2],p_dict['Mercury'][3],(p_dict['Mercury'][3]*YrS),(p_dict['Mercury'][4]*Me),p_dict['Mercury'][5],p_dict['Mercury'][6]))
print("")

print("Venus:")
print(Planets % (p_dict['Venus'][1],p_dict['Venus'][2],p_dict['Venus'][3],(p_dict['Venus'][3]*YrS),(p_dict['Venus'][4]*Me),p_dict['Venus'][5],p_dict['Venus'][6]))
print("")

print("Earth:")
print(Planets % (p_dict['Earth'][1],p_dict['Earth'][2]],p_dict['Earth'][3],(p_dict['Earth'][3]*YrS),(p_dict['Earth'][4]*Me),p_dict['Earth'][5],p_dict['Earth'][6]))
print("")

print("Mars")
print(Planets % (p_dict['Mars'][1],p_dict['Mars'][2],p_dict['Mars'][3],(p_dict['Mars'][3]*YrS),(p_dict['Mars'][4]*Me),p_dict['Mars'][5],p_dict['Mars'][6]))
print("")

print("Jupiter:")
print(Planets % (p_dict['Jupiter'][1],p_dict['Jupiter'][2],p_dict['Jupiter'][3],(p_dict['Jupiter'][3]*YrS),(p_dict['Jupiter'][4]*Me),p_dict['Jupiter'][5],p_dict['Jupiter'][6]))
print("")

print("Saturn:")
print(Planets % (p_dict['Saturn'][1],p_dict['Saturn'][2],p_dict['Saturn'][3],(p_dict['Saturn'][3]*YrS),(p_dict['Saturn'][4]*Me),p_dict['Saturn'][5],p_dict['Saturn'][6]))
print("")

print("Uranus:")
print(Planets % (p_dict['Uranus'][1],p_dict['Uranus'][2],p_dict['Uranus'][3],(p_dict['Uranus'][3]*YrS),(p_dict['Uranus'][4]*Me),p_dict['Uranus'][5],p_dict['Uranus'][6]))
print("")

print("Neptune:")
print(Planets % (p_dict['Neptune'][1],p_dict['Neptune'][2],p_dict['Neptune'][3],(p_dict['Neptune'][3]*YrS),(p_dict['Neptune'][4]*Me),p_dict['Neptune'][5],p_dict['Neptune'][6]))
print("")

print("Dwarf Planets")
print("")

print("Ceres:")
print(Planets % (p_dict['Ceres'][1],p_dict['Ceres'][2],p_dict['Ceres'][3],(p_dict['Ceres'][3]*YrS),(p_dict['Ceres'][4]*Me),p_dict['Ceres'][5],p_dict['Ceres'][6]))

print("Plutoids")
print("")

print("Pluto")
print(Planets % (p_dict['Pluto'][1],p_dict['Pluto'][2],p_dict['Pluto'][3],(p_dict['Pluto'][3]*YrS),(p_dict['Pluto'][4]*Me),p_dict['Pluto'][5],p_dict['Pluto'][6]))
print("")

print("Haumea")
print(Planets % (p_dict['Haumea'][1],p_dict['Haumea'][2],p_dict['Haumea'][3],(p_dict['Haumea'][3]*YrS),(p_dict['Haumea'][4]*Me),p_dict['Haumea'][5],p_dict['Haumea'][6]))
print("")

print("Makemake")
print(Planets % (p_dict['Makemake'][1],p_dict['Makemake'][2],p_dict['Makemake'][3],(p_dict['Makemake'][3]*YrS),(p_dict['Makemake'][4]*Me),p_dict['Makemake'][5],p_dict['Makemake'][6]))
print("")

print("Eris")
print(Planets % (p_dict['Eris'][1],p_dict['Eris'][2],p_dict['Eris'][3],(p_dict['Eris'][3]*YrS),(p_dict['Eris'][4]*Me),p_dict['Eris'][5],p_dict['Eris'][6]))
print("")


print("")
print("Epoch")
print(Epoch)

#wait function
input()