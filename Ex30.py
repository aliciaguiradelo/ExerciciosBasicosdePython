p = float(input("Digite o preço da etiqueta:"))
print("Código Condição de pagamento \n 1 	À vista em dinheiro ou cheque, recebe 10% de desconto \n 2 	À vista no cartão de crédito, recebe 15% de desconto \n 3 	Em duas vezes, preço normal de etiqueta sem juros \n 4 	Em quatro vezes, preço normal de etiqueta mais juros de 10%")
o = int(input("Digite a opção desejada:"))
if (o==1):
    print("O preço final,com 10% de desconto, é:", p*0.9)
elif (o==2):
    print("O preço final, com 15% de desconto, é:", p*0.85)
elif (o==3):
    print("O preço final é:", p)
elif (o==4):
    print("O preço final, com 10% de juros, é:", p*1.10)
else:
    print("Opção inválida!")