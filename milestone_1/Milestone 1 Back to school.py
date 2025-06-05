import math

eq = '4x^2 +4x +    (-8) =  0'
eq = eq.replace(' ', '')
eq = eq.split('=', )[0]
a = eq.split('+', )[0]
a = int(a.replace('x^2', '').replace('(', '').replace(')', ''))

b = eq.split('+', )[1]
b = int(b.replace('x', '').replace('(', '').replace(')', ''))
c = eq.split('+', )[2]
c = int(c.replace('(', '').replace(')', ''))
print(a, b, c)


x1 = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)


print(x1, x2) # 1 -2