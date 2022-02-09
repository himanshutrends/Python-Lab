def fact(n):
    factorial=1
    for i in range(1, n+1):
        factorial*=i
        i+=1
    return factorial

n=int(input("Enter a no."))
ans=fact(n)
print(ans)