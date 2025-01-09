import matplotlib

import matplotlib.pyplot as plt

import matplotlib.ticker as mticker 

import matplotlib.dates as mdates

import numpy as np

import time 

def bytespdate2num(b):
    return mdates.datestr2num(b.decode('utf-8'))

date, bid, ask = np.loadtxt("GBPUSD1d.txt", unpack= True, delimiter= ',', 
                                converters= {0 : bytespdate2num})

def percent_change(start, current): 
    x = ((float(current) - start) / start) * 100.00

    return x







def patternFinder():
    avgLine = ((bid + ask)/ 2)
    x = len(avgLine) - 30
    #Finds the pattern of 10 points previous to the data, to decide what is coming up next
    y = 11; 
    while y < x: 
        p1 = percent_change(avgLine[y - 10], avgLine[y - 9])
        p2 = percent_change(avgLine[y - 10], avgLine[y - 8])
        p3 = percent_change(avgLine[y - 10], avgLine[y - 7])
        p4 = percent_change(avgLine[y - 10], avgLine[y - 6])
        p5 = percent_change(avgLine[y - 10], avgLine[y - 5])
        p6 = percent_change(avgLine[y - 10], avgLine[y - 4])
        p7 = percent_change(avgLine[y - 10], avgLine[y - 3])
        p8 = percent_change(avgLine[y - 10], avgLine[y - 2])
        p9 = percent_change(avgLine[y - 10], avgLine[y - 1])
        p10 = percent_change(avgLine[y - 10], avgLine[y])

        outcomeRange = avgLine[y+20: y+30]

        currentPoint = avgLine[y]

        reduce = lambda x, y : x+ y, outcomeRange/len(outcomeRange)

        print(reduce)
        print(currentPoint)
        print('____')

        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        y = y+ 1
    
        time.sleep(55)

       






    

def graphRawfx():
    
    
    dig = plt.figure(figsize= (10, 7))

    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan = 40, colspan= 40)

    ax1.plot(date, bid)

    ax1.plot(date, ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    
    ax1_2 = ax1.twinx()

    ax1_2.fill_between(date, 0, ask - bid, facecolor = 'g', alpha = 0.3)
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    plt.subplots_adjust(bottom = 0.23)


    plt.grid(True)

    plt.show()



#graphRawfx()
patternFinder()









