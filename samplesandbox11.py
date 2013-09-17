import sys
import __builtins__
import string
import numpy

#Alloocate the memory required for the sandbox environment to run
#Limit the memory for the usage

memory=1024

ulimit -v 1000
ulimit -v-h 1000

#create the sandbox environment in the form of an array

myArray=a[100][100]


#Reading the files present on the command line of the sandbox
for fn in sys.argv[1:]:
    try:
        fin = open(fn, 'r')
    except:
        (type, detail) = sys.exc_info()[:2]
        print "\n*** %s: %s: %s ***" % (fn, type, detail)
        continue
    print "\n*** Contents of", fn, "***"
    
    # Print the file, with line numbers.
    lno = 1
    while 1:
        line = fin.readline()
        if not line: break;
        print '%3d: %-s' % (lno, line[:-1])
        lno = lno + 1
    fin.close()
print


#input is defined by the string function

s1='''enter the input value'''

#verifing the input is a polynomial

def polyval(s1, coef):
    #Evaluate at x the polynomial with coefficients given in coef#
    #The value s1 is returned #

    sum = 0
    while 1:
        sum = sum + coef[0]     # Add the next coef.
        coef = coef[1:]         # Done with that one.
        if not coef: break      # If no more, done entirely.
        sum = sum * s1          # Mult by x (each coef gets x right num times)

    return sum

#sandbox execution sample program fibonacci series


a, b = 0, 1

while a < s1:
    
    print(a)
    
    a,b=b,a+b
    
