dado = (input('Digite algo: '))
print(f'O dado apresentado é alfabético?', (dado.isalpha()))
print(f'O dado apresentado é numérico?', (dado.isnumeric()))
print(f'O dado apresentado é alfanumérico?', (dado.isalnum()))
print(f'O dado apresentado só tem espaços?', (dado.isspace()))
print(f'O dado apresentado está em minúsculas?', (dado.islower()))
print(f'O dado apresentado possui letra(s) maiúscula(s)?', (dado.isupper()))
print(f'O dado apresentado está em capitalizado?', (dado.istitle()))
print(f'O tipo primitivo desse dado é?', type(dado))

