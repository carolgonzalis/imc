def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o IMC com base no peso (kg) e altura (m)."""
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    """Classifica o IMC de acordo com a tabela da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Erro: Insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()
