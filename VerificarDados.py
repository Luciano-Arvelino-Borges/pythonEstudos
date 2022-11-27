dado = (input('Digite algo: '))
print(f'O dado apresentado é letra?', (dado.isalpha()))
print(f'O dado apresentado é número?', (dado.isnumeric()))
print(f'O dado apresentado é alfanumérico?', (dado.isalnum()))
print(type(dado))

