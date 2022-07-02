
print('-=*20')
print('Analisador de Triângulo')
print('-=*20')
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('segundo seguimento:'))
r3 = float(input('terceiro seguimento:'))
if r1 < r2 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima não podem formar um triânglo')