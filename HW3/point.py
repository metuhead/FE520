

import math

##Define the class
class pointcord:

    x,y=0,0
    

    def __init__(self, xpoint,ypoint):

        self.xpoint=xpoint

        self.ypoint=ypoint



    def distance(self):

        dist=math.sqrt((self.ypoint-0)**2 + (self.xpoint-0)**2)

        return dist


## Test the program
if __name__=="__main__":
    test_point= pointcord(0.9,0.6)
    print(test_point.distance())