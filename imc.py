def calcular_imc():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    imc = peso / altura**2
    return imc


resultado_imc = calcular_imc()
resultado_imc = round(resultado_imc, 2)
print("Seu IMC é:", resultado_imc)

if resultado_imc < 18.5:
    classificacao = "Magreza"
elif resultado_imc < 24.9:
    classificacao = "Normal"
elif resultado_imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print("Classificação do IMC:", classificacao)
