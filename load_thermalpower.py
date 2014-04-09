import numpy
import datetime
from dateutil.relativedelta import relativedelta

# Set time period under consideration (currently November 2013):
period_start = datetime.datetime.strptime('2013-Nov-01 00:00', '%Y-%b-%d %H:%M')
period_end = datetime.datetime.strptime('2013-Nov-30 23:59', '%Y-%b-%d %H:%M')
    
# Read thermal power datafile and create output file with only necessary data:
data = numpy.genfromtxt('thermal_power_201311.csv', dtype=str, delimiter=',')
outfile = open('thermal_power' + '.dat', 'w')
current = period_start
for row in data:
    if row[0] == 'Timestamp':
        continue
    rowtime = datetime.datetime.strptime(row[0][0:17],'%Y-%b-%d %H:%M')
    # Downsample (currently to only one observation per quarter of an hour):
    if rowtime >= current and rowtime <= period_end:
        outfile.write(row[1] + ' ' + row[4] + '\n')
        #print('Rowtime:' + str(rowtime) + ', ' + str(current))
        #current = current + relativedelta(hours=1)
        current = current + relativedelta(minutes=15)
        if rowtime > current:
            print(str(rowtime) + ', ' + str(current))
outfile.close()