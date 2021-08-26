

import time 
from generator import LCG
from generator import SCG
from point import pointcord


time_start=time.time()


LCG_test= LCG(2,1103515245,12345,2**32)

LCG_X=LCG_test.seqrandom(2000)

LCG_test= LCG(3,1103515245,12345,2**32)

LCG_Y=LCG_test.seqrandom(2000)


value=0

for i in LCG_X:
    
    for j in LCG_Y:

        dot=pointcord(i,j)
        
        if dot.distance()<=1:

            value=value+1

ratio=value/1000000

print(ratio)

ratio_difference= abs(ratio- 0.78539816339)

print(ratio_difference)





SCG_test= LCG(2,1103515245,12345,2**32)

SCG_X=LCG_test.seqrandom(2000)

SCG_test= LCG(3,1103515245,12345,2**32)

SCG_Y=LCG_test.seqrandom(2000)


value=0

for i in SCG_X:
    
    for j in SCG_Y:

        dot=pointcord(i,j)
        
        if dot.distance()<=1:

            value=value+1

ratio=value/1000000

print(ratio)

ratio_difference= abs(ratio- 0.78539816339)

print(ratio_difference)



print("Total seconds spent to get result is",time.time()-time_start)


