valor = float(input("Informe o valor do produto R$: "))
pagamento = int(input("Informe a forma de pagamento: \n [1] À VISTA DINHEIRO/CHEQUE \n [2] CARTÃO DE CRÉDITO \n "))

print(f"O valor do produto é de R${valor} e por conta do pagamento", end='')
if pagamento == 1:
    preco =  -(10 / 100 * valor)
    print(f"Você terá um desconto de 10%, totalizando assim um preço de R${preco:.2f}")
elif pagamento == 2:
    pagamento = int(input(" você terá que escolher qual opção deseja: \n [1] PAGAMENTO À VISTA \n [2] PAGAMENTO PARCELADO EM 2X \n [3] PAGAMENTO PARCELADOEM 3X OU MAIS \n "))
    if pagamento == 1:
        preco = valor - (5/100 * valor)
        print(f"Você terá um desconto de 5%, totalizando assim um preço de R$ {preco:.2f}")
    elif pagamento == 2:
        preco = valor
        valor /= 2
        print(f"Pela sua forma de pagamento você não terá desconto, totalizando assim duas parcelas de R$ (valor) e um valor de total de R${preco}")
    elif pagamento == 3:
        pagamento = int(input("Informe quantas parcelas serão utilizadas: "))
        preco = (20/100 * valor) + valor
        valor = preco / pagamento
        
        print(f"Devido a sua forma de pagamento em {pagamento}x de R${valor}, você terá um juros de R${20/100*valor} totalizando assim um preço de R${preco}")
else:
    print("Digite uma opção válida")