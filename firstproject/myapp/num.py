def cal(no1, no2):
    add=no1+no2
    sub=no1-no2
    mul=no1*no2
    div=no1//no2
    return add, sub, mul, div

n=cal(10, 5)
for x in n:
    print(x)


