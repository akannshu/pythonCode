
def fact(a):
    f = 1
    for i in range(1,a+1):
        f=f*i
    return f    



n = int(input())
c = fact(n)
d = fact(10)
e = fact(12)
print(c)
print(e)
print(d)

