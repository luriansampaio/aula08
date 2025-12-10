# Atividade - Dicionários e Listas (vendas)

# Crie um programa no Python que cadastre os dados de 3 vendedores. Cada vendedor deve ser amarzenado contendo as seguintes informações: 
# nome, 
# vendas - armazenar 5 vendas, representando os valores das vendas realizadas
# total - armazenar a soma de todas as vendas (calcular)
# media - armazenar a média das vendas (calcular)
# Após o cadastro dos 3 vendedores, o programa deve exibir os dados completos de cada um: Nome, lista das vendas, total e media 

vendedores = []

for v in range(3):
    print(f'\n -- vendedor {v + 1} -- ' )  
    nome = input('Informe o nome do vendedor:' )

    vendas = []
    for i in range(5):
        venda = float(input(f'Informe o valor da venda {i + 1}: '))
        vendas.append(venda)

    total = sum(vendas)

    media = sum(vendas) / len(vendas)

    vendedor = {
        'Nome': nome,
        'Vendas': vendas,
        'Total': total, 
        'Media': media 
    }

    vendedores.append(vendedor)

    # Exibindo os dados:
for s in vendedores:
        print(f'Nome: {s["Nome"]}')
        print(f'Vendas:{s["Vendas"]}')
        print(f'Total:{s["Total"]}')
        print(f'Media:{s["Media"]}\n')