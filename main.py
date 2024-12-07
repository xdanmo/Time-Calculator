import math

n = int(input('Enter the no. of value you want to Add: '))

a = []
b = []
c = []

for i in range(n):
    x = float(input('\nEnter the value of Hour: '))*3600
    y = float(input('Enter the value of Minutes: '))*60
    z = float(input('Enter the value of Second: '))
    a.append(x)
    b.append(y)
    c.append(z)
    
ts = sum(a + b + c)

h = math.floor(ts/3600)
rt = ts % 3600
m = math.floor(rt/60)
s = rt%60

print('\nHours: ',h)
print('Minutes: ',m)
print('Seconds: ',s)

print('\n>>>',h,':',m,':',s)
