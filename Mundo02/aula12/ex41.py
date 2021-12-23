from datetime import date
AnoNascimento = int(input("Informe o ano de nascimento do atleta: "))
Idade = date.today().year - AnoNascimento

print(f"O atleta tem {Idade} anos")
if Idade <= 9: print("Categoria Mirim")
elif Idade <= 14: print("Categoria Infantil")
elif Idade <= 19: print("Categoria Junior")
elif Idade <= 20: print("Categoria Sênior")
elif Idade > 20: print("Categoria Master")