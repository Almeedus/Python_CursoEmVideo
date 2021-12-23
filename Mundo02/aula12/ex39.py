from datetime import date
AnoNascimento = int(input("Informe o seu ano de nascimento: "))
idade = date.today().year - AnoNascimento
anos = 18 - idade
if anos < 0: anos *= -1

if idade > 18: print(f"Já passou {anos} anos da data que você deveria ter se alistado")
elif idade == 18: print("Agora é tempo de se alistar")
elif idade < 18: print(f"Faltam {anos} anos para se alistar")