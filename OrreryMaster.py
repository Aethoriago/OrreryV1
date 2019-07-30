#https://github.com/Aethoriago/OrreryV1/blob/master/README.md
#https://eyes.nasa.gov/apps/orrery/
#https://ssd.jpl.nasa.gov/?email_list
#https://solarsystem.nasa.gov/overlay-orrery/
#https://www.epochconverter.com/
#https://en.wikipedia.org/wiki/Eccentricity_(mathematics)
#https://technology.nasa.gov/patent/NPO-TOPS-26
#    [https://www.princeton.edu/~willman/planetary_systems/Sol/]

import time


AU = 149597870700
Yr = 365.25
YrS = 31557600
Me = 5974200000000000000000000
    #Note that Me is Mass relative to Earth Mass I.E 1Me = same mass as Earth. The string output is the actual mass however.
Epoch = time.time()


p_dict = {
    #'Planet' : [0, SmA, Ecc, OP, Me, PH, AH],
    'Mercury': [0.3870993, 0.20564, 0.2408467, 0.2408467*YrS, 0.05527*Me, 46001009, 69817445],
    'Venus' : [0.023336, 0.00678, 0.61519726, 0.61519726*YrS, 0.81500*Me, 107476170, 108942780],
    'Earth' : [1.000003, 0.01671, 1.0000174, 1.0000174*YrS, 1.0000*Me, 147098291, 152098233],
    'Mars' : [1.52371, 0.09339, 1.8808158, 1.8808158*YrS, 0.10745*Me, 206655215, 249232432], # note that Ceres is between Mars and Jupiter
    'Jupiter' : [5.2029, 0.0484, 11.862615, 11.862615*YrS, 317.83*Me, 740679835, 816001807],
    'Saturn' : [9.537, 0.0539, 29.447498, 29.447498*YrS, 95.159*Me, 1349823615, 1503509229],
    'Uranus' : [19.189, 0.04726, 84.016846, 84.016846*YrS, 14.5*Me, 2734998229, 3006318143],
    'Neptune' : [30.0699, 0.00859, 164.79132, 164.79132*YrS, 17.204*Me, 4459753056, 4537039826],
    'Ceres' : [2.7658, 0.078, 4.59984, 4.59984*YrS, 0.00016*Me, 380951528, 446428973],
    'Pluto' : [39.4821, 0.24883, 248.0208, 248.0208*YrS, 0.00220*Me, 4436756954, 7376124302],
    'Haumea' : [43.34, 0.189, 285.4, 285.4*YrS, 0.00070*Me, 5157623774, 7706399149],
    'Makemake' : [45.79, 0.159, 309.9, 309.9*YrS, 0.0007*Me, 5671928586, 7894762625],
    'Eris' : [67.67, 0.44177, 557.2, 557.2*YrS, 0.00278*Me, 576732799, 14594512904]
}

# implement  'for loop' for planet info

Planets = "| SemimajorAxis: %r AU | Eccentricity: %r | Orbital Period: %r Years(%r Years in Seconds) | Mass(kg): %r | Perihelion (km) %r | Aphelion (km) %r |"

for key in p_dict:
    print(key+":")
    print(Planets % tuple(p_dict[key])+'\n')

print(Epoch)

#wait function
input()