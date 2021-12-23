nome = str(input("Qual é o seu nome?"))

if nome == 'Gustavo':
    print("Que nome bonito")
elif nome == 'Eduardo':
    print("Seu nome é perfeito")
elif nome in 'Ana Claudia Juliana':
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia, {}.".format(nome))