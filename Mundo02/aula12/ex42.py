reta1 = float(input("Informe o valor do PRIMEIRO segmento: "))
reta2 = float(input("Informe o valor do SEGUNDO segmento: "))
reta3 = float(input("Informe o valor do TERCEIRO segmento: "))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print("Os segmentos FORMAM um triangulo", end=' ')
    
    if reta1 == reta2 and reta2 == reta3:
        print("EQUILÁTERO")
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print("ESCALENO") 
    else:
        print("ISÓCELES")
else: 
    print("Os segmentos NÃO FORMAM um triangulo")