x = int(input("Digite um número qualquer:"))

while (x<=0):
    print("Número inválido!")
    x = int(input("Digite outro número:"))
intervalo1 = int(input("Digite o primero valor do intervalo:"))
intervalo2 = int(input("Digite o segundo valor do intervalo:"))
while (intervalo1>intervalo2):
    print("Segundo intervalo inválido")
    intervalo2 = int(input("Digite o segundo intervalo novamente:"))
while(intervalo1<=intervalo2):
    t=x*intervalo2
    print(f"{x} X {intervalo2} = {t}")
    intervalo2=intervalo2-1