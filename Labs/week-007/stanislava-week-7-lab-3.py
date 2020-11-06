import sys
add = 0
n = len(sys.argv) 
  
for i in range(1, n): 
    add += int(sys.argv[i]) 
    print ("The sum is :", add)


#if __name__ == "__main__":
#    print(__name__)