print('Vamos calcular o IMC')
peso = float(input('Olá jovem! Por favor insira seu peso em kg: '))
altura = float(input('Por favor insira sua altura em metro: '))
resultado = peso / altura**2
print('O seu IMC é {:.2f}'.format(resultado)) #<{:.2f}.format é para deixar apenas dois numeros apos a virgula
if resultado < 18.5:
    print('Você está abaixo do peso')
elif resultado > 18.5 and resultado < 24.9:
    print('Você está normal')
elif resultado > 24.9 and resultado < 30:
    print('Sobrepeso')
else:
    print('Obesidade')