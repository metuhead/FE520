##### Q1




###Q1.1

## Creating a Rectangular Class
class Rectangular:

## Creating a constructor  
    def __init__(self,length,width):
        self.length=length
        self.width=width
## Creating an area method to return the area of rectangular   
    def area(self):
        
        return self.length*self.width
## Creating a perimeter method to return the perimeter of rectangular   
    def perimeter(self):

        return 2*self.length+2*self.width


# Test the Rectangular class
myRec = Rectangular(10,20)

print(myRec.area())


print(myRec.perimeter())


###Q1.2

import numpy as np

# Define length and width
length=np.array([1,3,5,7,9,11,13,15,17,19])
width=np.array([2,4,6,8,10,12,14,16,18,20])

# Use lenght and width as a argument in Rectangular function
test_rect=Rectangular(length,width)

# Print out the results to see test the code
print(test_rect.area())

print(test_rect.perimeter())



##### Q2



class Time:

    
    ## Creating a constructer 

    def __init__(self,hours,minutes,seconds):
        
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
        self.timehour=self.hours
        self.timemin=self.minutes
        self.timesec=self.seconds


    ## Adding time to the time given in constructer
    def addTime(self,h,m,s):

        self.h=h
        self.m=m
        self.s=s

        totsec=self.seconds+self.s

        if totsec<60:
            self.timesec=totsec
            sec_excess=0
        if totsec>=60:
            self.timesec=totsec-60
            sec_excess=1

        totmin=self.minutes+self.m+sec_excess

        if totmin<60:
            self.timemin=totmin
            min_excess=0
        if totmin>=60:
            self.timemin=totmin-60
            min_excess=1

        self.timehour=self.hours+self.h+min_excess

    #### Test the class
        print(self.timehour,self.timemin,self.timesec)
    ### Displating the time in order of (hours,minutes,seconds)
    def displayTime(self):

        print(self.hours,"hours",self.minutes,"minutes",self.seconds,"seconds")

    ### Displaying total seconds of the time given
    def DisplaySecond(self):

        display_second= (self.timehour*3600)+(self.timemin*60)+self.timesec

        return display_second




###Testing the program
if __name__=="__main__":

    time=Time(1,2,0)

    time.displayTime()
#time.addTime(1,10,10)

    time.addTime(1,38,27)

    time.DisplaySecond()




