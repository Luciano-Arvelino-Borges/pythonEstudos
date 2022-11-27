idade = int(input('Digite sua idade: '))
if idade <16:
    print('Voto Proibido')
elif (idade >=16 and idade <18) or (idade > 70):
    print('Voto Facultativo')
else:
    print('Voto Obrigatório')



