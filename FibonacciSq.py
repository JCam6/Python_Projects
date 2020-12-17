# Dynamic Programming sample using Fibonacci's sequence.
# System recursion limit will bound program response near a 130 digit integer.

def main():


    posiiton = int(input("What posiiton in Fibonacci's sequence would you like to find? "))
    result = fib(posiiton)  
    print(result) 

def fib(n, m = {}):
    if n in m:
        return m[n]
    else:
        if n <= 2:
            return 1
        else:
            m[n] = fib(n - 1, m) + fib(n - 2, m)
            return m[n]



main()
