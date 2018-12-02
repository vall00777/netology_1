znak, a, b = input().split()
try:
     if znak == '+':
          print(float(a)+float(b))
     elif znak == '-':
          print(float(a)-float(b))
     elif znak == '*':
          print(float(a)*float(b))
     elif znak == '/':
          print(float(a)/float(b))
 except ZeroDivisionError:
     print("На ноль делить нельзя")
