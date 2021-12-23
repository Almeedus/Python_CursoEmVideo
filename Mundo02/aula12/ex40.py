Nota1 = float(input("Informe a primeira nota do aluno:"))
Nota2 = float(input("Informe a segunda nota do aluno:"))

Media = (Nota1 + Nota2) / 2

if Media < 5.0: print(f"O aluno foi reprovado com uma média de {Media:.1f}")
elif Media >= 5.0 and Media <= 6.9: print(f"O aluno está em recuperação com uma média de {Media:.1f}")
elif Media > 7.0: print(f"O aluno foi aprovado com uma média de {Media:.1f}")