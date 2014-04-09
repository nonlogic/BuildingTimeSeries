import os
import numpy
import datetime
from dateutil.relativedelta import relativedelta

# Get names of all files in directory:
path = './20130801-20140119/VAV Terminal Units/'
filenames = os.listdir(path)

# Set time period under consideration (currently November 2013).
period_start = datetime.datetime.strptime('2013-11-01T00:00', '%Y-%m-%dT%H:%M')
period_end = datetime.datetime.strptime('2013-11-30T23:59', '%Y-%m-%dT%H:%M')

# For each of the files in the directory, perform:
for filename in filenames:
    # Only read files which have the Tzone values:
    if 'Zone Temperature' in filename:
        print(filename) # Keep track of which file is being read.
        # Read file, and write relevant data into output file called ZONE.dat:
        data = numpy.genfromtxt(path + filename, dtype=str, delimiter=',')
        outfile = open(path + filename[0:4] + '.dat', 'w')
        current = period_start
        for row in data:
            if row[0] == 'timestamp':
                continue
            rowtime = datetime.datetime.strptime(row[0][0:16],'%Y-%m-%dT%H:%M')
            # Downsample (currently, to only one observation per hour):
            if rowtime >= current and rowtime <= period_end:
                outfile.write(row[1] + '\n')
                #current = current + relativedelta(hours=1)
                current = current + relativedelta(minutes=15)
        outfile.close()