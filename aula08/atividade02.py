# Atividade inicial
#Utilizando função, desenvolva um algoritmo, que solicite ao usuário, o preço e a quantidade referente a 3 vendas. 
#Para cada venda, o sistema deve calcular o valor total e exibir o resultado.

# A forma que eu fiz:


# def somar_vendas(a, b, c):
#     total_de_vendas = a + b + c
#     print(total_de_vendas)



# for v in range(3):
#     v1 = float(input('Digite o valor da primeira venda: '))
#     v2 = float(input('Digite o valor da segunda venda: '))
#     v3 = float(input('Digite o valor da terceira venda:  '))
#     somar_vendas(v1, v2, v3)


# def somar_quantidades(x,y,z):
#     quantidade_total = x + y + z
#     print(quantidade_total)  


# for q in range(3):
#     q1 = float(input('Digite a quantidade da primeira venda: '))
#     q2 = float(input('Digite a quantidade da segunda venda: '))   
#     q3 = float(input('Digite a quantidade da teceira venda: '))
#     somar_quantidades(q1, q2, q3)

# for vt in range(3):
#     resultado1 = q1 * v1 
#     resultado2 = q2 * v2
#     resultado3 = q3 * v3
#     print(f'Os resultados finais das vendas respectivamente são: {resultado1}, {resultado2} e {resultado3}')


# A forma que o professor recomenda:


def calcula_total(v, q):
    t = v * q 
    print(f'O total é {t}. ')
    return t 



for i in range(3):
    venda = float(input('Informe o valor da venda: '))
    qtd = float(input('Informe a quantidade do produto: '))
    total = calcula_total(venda,  qtd)
    print(f'Valor total é: {total}')




    


