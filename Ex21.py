a = float(input("Digite o primeiro valor:"))
b = float(input("Digite o segundo valor:"))

m = a*b
ad = a+b
d = a/b
s = a-b 

print("\nMENU\n")
print("1.Multiplicação \n2.Adição \n3.Divisão \n4.Subtração \n5.Fim do processo \n" )

c = int(input("Digite o número da opção desejada:"))

if (c==1):
    print(f"O resultado da multiplicação é:{m:.2f}")
elif (c==2):
    print(f"O resultado da adição é:{ad:.2f}")
elif (c==3):
       if (b==0):
        print("ERRO!")
       else:
        print(f"O resultado da divisão é:{d:.2f}")
elif (c==4):
    print("O resultado da adição é:{ad:.2f}")
elif (c==5):
    print("Fim do programa!")
else:
    print("Opção inválida!")
