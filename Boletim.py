nome = str(input('Digite o nome do aluno: '))
tel = str(input('Digite o telefone do aluno ou responsável: '))
serie = str(input('Digite a série do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quartaa nota: '))
media = (nota1+nota2+nota3+nota4)/4
print('----------Curso EAD----------')
print(f'Nome: {nome}; Telefone: {tel}; Série: {serie}')
if media >= 7:
    print(f'A média do aluno {nome} é {media}. APROVADO!')
else:
    print(f'A média do aluno {nome} é {media}. REPROVADO')
