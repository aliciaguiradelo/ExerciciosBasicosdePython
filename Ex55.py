novamente = "s"
valores = []

qnt = int(input("Digite a quantidade de valors a serem digitados:"))
while(qnt<=0 or qnt>20):
    print("Opa! O limite é até 20!")
    qtd = int(input("Digite a quantidade de valores a serem digitados:"))
for i in range(0,qnt,1):
    x = int(input("Digite um valor:"))
    valores.append(x)
while(novamente =="s"):
    num = int(input("Digite um número para ser localizado no array:"))
    pos = -1
    print("Lembrando que as posições começam com o 0!")

    for i in range(0, qnt,1):
        if (valores[i]==num):
            pos=i
    if(pos!=-1):
        print("O valor foi encontrado na posição:", pos)
    else:
        print("Valor não encontrado")
    novamente=input("Deseja realizar uma nova consulta?(S/N):")
print("Obrigada!")