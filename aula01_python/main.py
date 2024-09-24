# print("Numero de caracteres no nome: ", len(input("Digite seu nome: ")))

# a = int(input("Insira um valor: "))
# b = int(input("Insira outro valor: "))

# print("A soma destes valores é: ", a+b)

CONSTANTE_BONUS = 1000

nome = input('Digite seu nome: ')

salario = round(float(input('Digite seu salário: ')),2)

bonus = round( float(input('Digite O valor do bonus: ')),2)

valor_final = CONSTANTE_BONUS + (salario * bonus)

print(f'Resultado: {CONSTANTE_BONUS} +', salario * bonus )

print( f'Olá {nome}, o seu valor de bônus foi de {valor_final}')