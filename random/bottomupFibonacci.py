
def fib(n): 

    f = [0]*(n+1)

    f[1] = 1

    for i in xrange(2 , n+1): 

        f[i] = f[i-1] + f[i-2] 

    return f[n]  

def main(): 
	

    n = 9

    print ("Fibonacci number is " , fib(n)) 