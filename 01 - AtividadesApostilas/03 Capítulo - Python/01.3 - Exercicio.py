#Crie um programa que peça ao usuário para digitar o valor total de uma venda, 
#o percentual de desconto aplicado e o percentual de imposto cobrado. Ao fim, o programa 
#deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

valor_total = float(input("Digite o valor total da venda: "))
desconto_percentual = float(input("Digite o percentual de desconto: "))

valor_desconto = valor_total * (desconto_percentual / 100)
valor_com_desconto = valor_total - valor_desconto

imposto_percentual = float(input("Digite o percentual de imposto: "))

valor_imposto = valor_com_desconto * (imposto_percentual / 100)
preco_final = valor_com_desconto + valor_imposto

print(f"O preço final do produto, após o desconto e inclusão de impostos, é R$ {preco_final:.2f}")



