# just trying to generate the longest list possible whilst following the rules
# try each possibility and see how long the list it creates is, maybe have two list storing the longest list 
# found and the current list and compare the two and remove the shorter one, 
# then use the empty list to try the next possibility
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
print(numpy.argsort(listOfPeaks))   # out [23 7 11 0 1 25 24 10 12 29 27 4 13 8 14 15 9 16 19 28 26 30 3 18 21 5 6 20 17 22 2]