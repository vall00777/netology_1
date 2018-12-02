try:
     znak, a, b = input().split()
except ValueError:
     print("Неверный ввод")
else:
     try:
          assert float(a) > 0 and float(b) > 0
     except AssertionError:
          print('Число меньше 0')
     if znak == '+':
          print(float(a)+float(b))
     elif znak == '-':
          print(float(a)-float(b))
     elif znak == '*':
          print(float(a)*float(b))
     elif znak == '/':
          print(float(a)/float(b))
