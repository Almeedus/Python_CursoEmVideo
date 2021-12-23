ValorCasa = float(input("Informe o valor da casa: "))
Salario = float(input("Informe o seu salário em R$: "))
PrestacaoAnual = int(input("Informe em quantos anos deseja pagar: "))

PrestacaoAnual *= 12
PrestacaoMensal = ValorCasa / PrestacaoAnual
CalculoAprovacao = (30/100) * Salario

if CalculoAprovacao >= PrestacaoMensal:
    print("="*60)
    print("O valor foi APROVADO para a compra da casa!")
    print(f"O valor da prestação em {PrestacaoAnual} anos equivale a {PrestacaoMensal:.2f} por mes")
    print("="*60)
else:
    print("="*60)
    print("O valor foi NEGADO para compra da casa!")
    print(f"O valor da prestação em {PrestacaoAnual} anos equivale a {PrestacaoMensal:.2f} por mes")
    print("="*60)