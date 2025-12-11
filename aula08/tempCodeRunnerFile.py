def calcula_total(v, q):
    t = v * q 
    print(f'O total é {t}. ')



for i in range(3):
    venda = float(input('Informe o valor da venda: '))
    qtd = float(input('Informe a quantidade do produto: '))
    calcula_total(venda,  qtd)

