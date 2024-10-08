CONSTANTE_BONUS = 1000

nome = input('Digite seu nome: ')

if nome.isdigit():
    print('Você digitou seu nome errado')
    exit()
elif len(nome) == 0:
    print('Você não digitou nada!')
    exit()

salario = round(float(input('Digite seu salário: ')),2)

bonus = round( float(input('Digite O valor do bonus: ')),2)

valor_final = CONSTANTE_BONUS + (salario * bonus)

print(f'Resultado: {CONSTANTE_BONUS} +', salario * bonus )

print( f'Olá {nome}, o seu valor de bônus foi de {valor_final}')