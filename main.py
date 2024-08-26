arquivos = ['teste1.txt', 'teste2.txt', 'teste3.txt']

for nome_arquivo in arquivos:
    try:
        with open(nome_arquivo, 'r') as f:
            linhas = f.readlines()
        total_operacoes = int(linhas[0].strip())
        posicao = 1
        resultados = []

        for _ in range(total_operacoes):
            codigo = linhas[posicao].strip()
            conjunto_a = set(linhas[posicao + 1].strip().split(','))
            conjunto_b = set(linhas[posicao + 2].strip().split(','))


            conjunto_a = {elemento.strip() for elemento in conjunto_a}
            conjunto_b = {elemento.strip() for elemento in conjunto_b}

            if codigo == 'U':
                resultado = conjunto_a.union(conjunto_b)
            elif codigo == 'I':
                resultado = conjunto_a.intersection(conjunto_b)
            elif codigo == 'D':
                resultado = conjunto_a.difference(conjunto_b)
            elif codigo == 'C':
                resultado = {(x, y) for x in conjunto_a for y in conjunto_b}
            else:
                resultado = "código de operação desconhecido"

            resultados.append(f"resultado da operacao {codigo} no arquivo {nome_arquivo}: {resultado}")

            posicao += 3


        print(" | ".join(resultados))

    except FileNotFoundError:
        print(f"erro: o arquivo {nome_arquivo} nao foi encontrado.")
    except Exception as erro:
        print(f"erro ao processar o arquivo {nome_arquivo}: {erro}")
