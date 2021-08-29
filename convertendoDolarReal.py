from forex_python.converter import CurrencyRates

c = CurrencyRates()

# Pergunta e insere o valor que deseja converter
vl = float(input("\n Qual o valor que deseja converter para real ?"))

# Converte e formate o resultado
r = round(c.convert("USD", "BRL", vl), 2)

# Mostrar o resultado
print(f"${vl} ={r}")
