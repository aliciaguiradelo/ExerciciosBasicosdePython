a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

if (a+b<c):
  print("A soma é %d + %d < %d " %(a,b,c))
elif (a+b>c):
  print("A soma é %d + %d > %d " %(a,b,c))
else:
  print("end")