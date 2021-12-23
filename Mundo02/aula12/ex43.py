peso = float(input("Informe o seu peso: (kg)"))
altura = float(input("Informe sua altura: (M)"))

IMC = peso / (altura ** 2)

print(f"Seu IMC é de {IMC:.1f}.",end='')
if IMC <= 1.85: 
    print("você está ABAIXO DO PESO!")
elif IMC <= 25:
    print("Você está no PESO IDEAL!")
elif IMC <= 30:
    print("Você está no SOBREPESO!")
elif IMC <= 40:
    print("Você está na OBESIDADE! TOME CUIDADO")
elif IMC > 40:
    print("Você está na OBESIDADE MÓRBIDA!!! CUIDADO")