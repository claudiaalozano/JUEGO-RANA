import math
import os
import random
import re
import sys

class coordenadas:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def comparate(self , x , y):
        if(self.x==x and self.y==y):
            return True
        else:
            return False


#if __name__ == '__main__':
#first_multiple_input = input().rstrip().split()
#n = int(first_multiple_input[0])
#m = int(first_multiple_input[1])
#k = int(first_multiple_input[2])

#for n in range(n):
    #row = input()


#for k_itr in range(k):
    #second_multiple_input = input().rstrip().split()
    #i1 = int(second_multiple_input[0])
    #j1 = int(second_multiple_input[1])
    #i2 = int(second_multiple_input[2])
    #j2 = int(second_multiple_input[3])