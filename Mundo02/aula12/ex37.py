NumeroInteiro = int(input("Informe um número inteiro: "))
print("Conversão de Base:\n [1] BINÁRIO\n [2] OCTAL\n [3] HEXADECIMAL") 
Escolha = int(input("Escolha qual base a conversão deve ser feita: "))

if Escolha == 1: print("Em Binário, o número {} equivale à {}".format(NumeroInteiro, bin(NumeroInteiro)[2:]))
elif Escolha == 2: print("Em Octal, o número {} equivale à {}".format(NumeroInteiro, oct(NumeroInteiro)[2:]))
elif Escolha == 3: print("Em Hexadecimal, o número {} equivale à {}".format(NumeroInteiro, hex(NumeroInteiro)[2:]))
else: print("É preciso digitar um número válido")
