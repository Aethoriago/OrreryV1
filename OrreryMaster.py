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


Ex = 1

AU = 149597870700
Yr = 365.25
YrS = 31557600
Me = 5974200000000000000000000
    #Note that Me is Mass relative to Earth Mass I.E 1Me = same mass as Earth. The string output is the actual mass however.
Epoch = time.gmtime(time.time())

#Planets
Planets = "| SemimajorAxis: %r AU | Eccentricity: %r | Orbital Period: %r Years(%r Years in Seconds) | Mass: %r |"

print("Planets")

#Mercury
MercurySmA = 0.3870993
MercuryEcc = 0.20564
MercuryOP = 0.2408467
MercuryMe = 0.05527
print("Mercury:")
Mercury = print(Planets % (MercurySmA,MercuryEcc,MercuryOP,(MercuryOP*YrS),(MercuryMe*Me)))

#Venus
VenusSmA = 0.023336
VenusEcc = 0.00678
VenusOP = 0.61519726
VenusMe = 0.81500
print("Venus:")
Venus = print(Planets % (VenusSmA,VenusEcc,VenusOP,(VenusOP*YrS),(VenusMe*Me)))

#Earth
EarthSmA = 1.000003
EarthEcc = 0.01671
EarthOP = 1.0000174
EarthMe = 1.0000
print("Earth:")
Earth = print(Planets % (EarthSmA,EarthEcc,EarthOP,(EarthOP*YrS),(EarthMe*Me)))

#Mars
MarsSmA = 1.52371
MarsEcc = 0.09339
MarsOP = 1.8808158
MarsMe = 0.10745
print("Mars")
Mars = print(Planets % (MarsSmA,MarsEcc,MarsOP,(MarsOP*YrS),(MarsMe*Me)))

#Jupiter
JupiterSmA = 5.2029
JupiterEcc = 0.0484
JupiterOP = 11.862615
JupiterMe = 317.83
print("Jupiter:")
Jupiter = print(Planets % (JupiterSmA,JupiterEcc,JupiterOP,(JupiterOP*YrS),(JupiterMe*Me)))

#Saturn
SaturnSmA = 9.537
SaturnEcc = 0.0539
SaturnOP = 29.447498
SaturnMe = 95.159
print("Saturn:")
Saturn = print(Planets % (SaturnSmA,SaturnEcc,SaturnOP,(SaturnOP*YrS),(SaturnMe*Me)))

#Uranus
UranusSmA = 19.189
UranusEcc = 0.04726
UranusOP = 84.016846
UranusMe = 14.5
print("Uranus:")
Uranus = print(Planets % (UranusSmA,UranusEcc,UranusOP,(UranusOP*YrS),(UranusMe*Me)))

#Neptune
NeptuneSmA = 30.0699
NeptuneEcc = 0.00859
NeptuneOP = 164.79132
NeptuneMe = 17.204
print("Neptune:")
Neptune = print(Planets % (NeptuneSmA,NeptuneEcc,NeptuneOP,(NeptuneOP*YrS),(NeptuneMe*Me)))

print("Dwarf Planets")

#Ceres
CeresSmA = 2.7658
CeresEcc = 0.078
CeresOP = 4.59984
CeresMe = 0.00016
print("Ceres:")
Ceres = print(Planets % (CeresSmA,CeresEcc,CeresOP,(CeresOP*YrS),(CeresMe*Me)))

print("Plutoids")


#Pluto
PlutoSmA = 39.4821
PlutoEcc = 0.24883
PlutoOP = 2480208
PlutoMe = 0.00220
print("Pluto")
Pluto = print(Planets % (PlutoSmA,PlutoEcc,PlutoOP,(PlutoOP*YrS),(PlutoMe*Me)))

#Haumea
HaumeaSmA = 43.34
HaumeaEcc = 0.189
HaumeaOP = 285.4
HaumeaMe = 0.00070
print("Haumea")
Haumea = print(Planets % (HaumeaSmA,HaumeaEcc,HaumeaOP,(HaumeaOP*YrS),(HaumeaMe*Me)))

#Makemake
MakemakeSmA = 45.79
MakemakeEcc = 0.159
MakemakeOP = 309.9
MakemakeMe = 0.0007
print("Makemake")
Makemake = print(Planets % (MakemakeSmA,MakemakeEcc,MakemakeOP,(MakemakeOP*YrS),(MakemakeMe*Me)))

#Eris
ErisSmA = 67.67
ErisEcc = 0.44177
ErisOP = 557.2
ErisMe = 0.00278
print("Eris")
Eris = print(Planets % (ErisSmA,ErisEcc,ErisOP,(ErisOP*YrS),(ErisMe*Me)))