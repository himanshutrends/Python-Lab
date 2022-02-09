def fib(n):
    t1=0
    t2=1
    
 
    for i in range(1, n+1):
        print(t1)
        aglaTerm=t1+t2
        t1=t2
        t2=aglaTerm

n=int(input("Enter a no."))
fib(n)