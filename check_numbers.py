#Napisz program
import sys
from sympy import isprime
if(len(sys.argv) > 1):
     if(sys.argv[1] != 0):
          filename = sys.argv[1]
else:
     filename = 0
     print("No file given.")
if(filename != 0):     
     file = open(filename, "r")
     line = file.readline()
     while( line != ''):
          splitedline = line.split()  
          splitedline[1] = int(splitedline[1],16)
          if(isprime(splitedline[1])):
               print (splitedline[0])
          line = file.readline()        
     file.close()
