import os
import numpy

# Add path to zone data directory and list files in the directory:
path = './20130801-20140119/VAV Terminal Units/'
filenames = os.listdir(path)

# Read Qcooling and Tsupply data:
data = numpy.loadtxt('thermal_power.dat')
print(data.shape)

# Read Tzone data from .dat files and append to matrix:
for filename in filenames:
    if '.dat' in filename:
        print(filename)
        zonedata = numpy.array([numpy.loadtxt(path + filename)]).T
        print(zonedata.shape)
        data = numpy.concatenate((data, zonedata), axis=1)

# Save matrix to file:
numpy.savetxt('matrix.dat', data)