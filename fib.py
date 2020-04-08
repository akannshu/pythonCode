def fib(n):
    arr = [0,1]
    for i in range(2,n+1):
        c = arr[i-1] + arr[i-2]
        arr.append(c)

    return arr    

n = int(input())
k = fib(n)
print(k)
