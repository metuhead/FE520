
class LCG:
    ###Creating a constructor 
    def __init__(self,seed,multiplier,increment,modulus):

        self.seed=seed
        self.multiplier=multiplier
        self.increment=increment
        self.modulus=modulus

    
    ### Creating setseed method
    def setseed(self, set):
        
        self.set=set
        return self.set
    ### Creating getseeds method
    def getseeds(self):
        
        return self.seed


    def initgen(self):

        value_zero=self.seed

    ### To create a uniform distributed sequence,  you only need to divide the  sequence above by M '''
        
        num1=value_zero /self.modulus
        return num1
    
    def formula(self,X):

        return (X*self.multiplier+self.increment)%self.modulus

    def nextrand(self):

        value_zero =self.seed
        value_one=self.formula(value_zero)

        num2= value_one/self.modulus
        return value_one

    def seqrandom(self,leng):

        seq_list= list()
        
        value_zero=self.seed
        num1=self.initgen()

        seq_list.append(num1)

        if leng<1:
            
            return "Incorrect Length "
        if leng==1:

            return seq_list

        else:

            for input in range(1,leng):

                value_i=self.formula(value_zero)

                NUMi= value_i/self.modulus

                seq_list.append(NUMi)

                value_zero=value_i
        return seq_list


## Test
##a=LCG(1,2,1,2)
##a.seqrandom(3)


class SCG(LCG):

    def initgen(self):
        if self.seed%4 is not 2:
    
            # print Error
            print("Error: Mod should be 2")
            
            return LCG.initgen(self)

    
    def formula(self,X):
           
       return ((( self.multiplier*((( self.multiplier*(X+1))+self.increment)%self.modulus))+self.increment)%self.modulus)%self.modulus       




## Test the code


if __name__=="__main__":
    
    zort1=LCG(0,1103515245,12345,2**32)


    zort1.setseed(1)

    print(zort1.getseeds())

    print(zort1.nextrand())

    print(zort1.initgen())

    
    print(zort1.seqrandom(2))


    zort2=SCG(3,1103515245,12345,2**32)

    print(zort2.getseeds())

    zort1.setseed(6)

    print(zort2.initgen())

    print(zort2.nextrand())

    print(zort2.seqrandom(5))








    
