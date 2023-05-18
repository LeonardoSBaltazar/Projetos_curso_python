nome = input('Digite seu Nome: ')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * altura)

if imc <= 24.9:
    print(f"{nome} Sua Classificação é Normal")
elif imc >= 25 and imc <= 29.9:
    print(f"{nome} Sua Classificação é Sobrepeso")
elif imc >= 30 and imc <= 40:
    print(f"{nome} Sua Classificação é Obesidade")
else:
    print(f"{nome} Sua Classificação é Obesidade Grave")

