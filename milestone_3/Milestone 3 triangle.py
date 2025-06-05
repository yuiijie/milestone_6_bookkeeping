from math import factorial

def get_triangle1(rows: int):
  triangle = []
  row = []
  last_row = []
  for i in range(rows):
    row = []
    for j in range(i+1):
      row.append((factorial(i)//(factorial(j)*factorial(i-j))))
    triangle.append(row)
    last_row = row

  return triangle


get_triangle1(5)


def get_triangle2(rows: int):
  n = 1
  for i in range(1, rows + 1):
    for o in range(1, rows - i+1):
        print(' ',end='')
    for j in range(0, i):
        if j==0 or i==0:
            n = 1
        else:
            n = n * (i - j)//j
        print(n, end = ' ')
    print()

  return get_triangle2

get_triangle2(5)
