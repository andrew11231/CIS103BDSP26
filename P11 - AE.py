#Andrew Espinoza
import time

genfiles = 'C:/temp/points.txt'
datagenfiles = open(genfiles,'r')
gradfiles = "C:/temp/gradess.txt"
datagradfiles = open(gradfiles,'w')
errorfiles = "C:/temp/errorrr.txt"
dataerrorfiles = open(errorfiles,'w')

line1 = datagenfiles.readline()
print(line1)
datagenfiles.close()
