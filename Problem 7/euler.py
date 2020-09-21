# What is the 10 001st prime number?

import math

def prime(n):
    if (n < 2):
        return 0
    if (n != 2 and n % 2 == 0):
        return 0
        
    x = math.floor(math.sqrt(n))    
    for d in range (3, x + 1, 2):
        if (n % d == 0):
            return 0
            
    return 1
        
if __name__ == "__main__":
    
    n = 1
    i = 1
    while (i != 10001):
        if (prime(n)):
            i += 1
            print(n)
        n += 2