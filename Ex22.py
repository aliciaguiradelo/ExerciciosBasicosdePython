print("\nMENU\n")
print("1.Triângulo \n2.Quadrado \n3.Retângulo \n4.Círculo \n5.Fim do processo \n" )

s = int(input("Digite a opção desejada:"))

if (s==1):
    a=float(input("Digite a altura do triângulo:"))
    b=float(input("Digite a base do triângulo:"))
    area1=a*b
    print("A área do triângulo é:", area1)
elif (s==2):
    l=float(input("Digite o lado do quadrado:"))
    area2=l*l
    print("A área do quadrado é:", area2)
elif (s==3):
    a1=float(input("Digite a altura do retângulo:"))
    b1=float(input("Digite a base do retângulo:"))
    area3=a1*b1
    print("A área do quadrado é:", area3)
elif (s==4):
    r=float(input("Digite o raio do círculo:"))
    area4=3.14*r
    print("A área do círculo é:", area4)
elif (s==5):
    print("Fim do processo!")
else:
    print("Opção inválida!")

    