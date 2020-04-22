#Napisz program
import sys
from sympy import isprime
if(len(sys.argv) > 1):
     if(sys.argv[1] != 0):
          filename = sys.argv[1]
else:
     filename = 0
     print("No file to check. Use 'python check_numbers.py filetocheckname.txt'")
if(filename != 0):     
     file = open(filename, "r")
     line = file.readline()
     result = "["
     while( line != ''):
          splitedline = line.split()  
          splitedline[1] = int(splitedline[1],16)
          line = file.readline()
          if(isprime(splitedline[1])):
               result = result + splitedline[0] 
               if(line != ''):
                    result = result + ", "
     file.close()
     print (result + "]")
