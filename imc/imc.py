# portfólio DEVELOPMENT TOOLS E CLOUD COMPUTING
# Desenvolvendo um programa de calculo de Indice de Massa Muscular

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros:"))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc}")

if imc < 18.5:
    print("Classificação: Abaixo do peso!")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal!")
elif 25 <= imc < 34.9:
    print("Classificação: Obesidade grau 1!")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau 2!")
else:
    print("Classificação: Obesidade grau 3!")
