# just trying to generate the longest list possible whilst foolowing the rules
# try each number and see how long the list it creates is
# select smallest number in first half and start from their
# potentially i could sort the numbers then find their original indexes later
import sys
import numpy

def plan_route(listOfPeaks):
    peaksVisited = 0

    for i in range(len(listOfPeaks) - 1):
        a = []
        b = []

        if a == []:
            a.append(listOfPeaks[i])
            continue     


        if listOfPeaks[i] <= a[- 1]:
            a.append(listOfPeaks[i])
      
        if i == (len(listOfPeaks) - 1):
            peaksVisited = len(a)

       
def plan_route2(listOfPeaks):

    a = numpy.argsort(listOfPeaks)




listOfPeaks = [1, 2, 20, 13, 6, 15, 16, 0, 7, 9, 4, 0, 4, 6, 7, 8, 10, 18, 14, 10, 17, 15, 19, 0, 4, 2, 12, 6, 10, 5, 12]
print(numpy.argsort(listOfPeaks))