import math as ma
def checker(n):
    if len(str(n))>3:
        for x in range(2,12):
            if n%x==0:
                return(print("Given number {} is not a prime number.".format(n)))
    sr = ma.ceil(ma.sqrt(n))
    for x in range(7,sr,6):
        if (n%x)==0:
            print(x)
            return(print("Given number {} is not a prime number.".format(n)))
    for x in range(5,sr,6):
        if (n%x)==0:
            return(print("Given number {} is not a prime number.".format(n)))
        
    return(print("Given number {} is a prime number.".format(n)))

        
if __name__=='__main__':
    #n = int(input())#uncomment to interactive input
    n = 10092003300140014003 #example 1
    n= 101234567890147467687 #example 2
    n= 143014298809          #example 3
    checker(n)
    
