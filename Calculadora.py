def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicita ao usuário para inserir o peso e a altura
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC
resultado_imc = calcular_imc(peso, altura)

# Classifica o IMC
classificacao = classificar_imc(resultado_imc)

# Exibe o resultado
print(f"Seu IMC é: {resultado_imc:.2f}")
print(f"Classificação: {classificacao}")
