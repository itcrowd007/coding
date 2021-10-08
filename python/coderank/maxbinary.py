import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #n = (bin(int(input().strip()))[2:]).split("0")
    print(sum(map(int,str(max((bin(int(input().strip()))[2:]).split("0"))))))
