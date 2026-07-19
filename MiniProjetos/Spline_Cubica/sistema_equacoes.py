import condicoes

def matriz_dos_coeficientes(x:list, condicao = 'natural')->list:
    '''
    Combina os coeficientes gerados pelas funções de condições para a montagem a matriz dos coeficientes para solucionar o sistema linear afim 
    de determinar os coeficientes de cada subfunção.
    
    Paramêtros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
        condicao (str): Tipo de condição a se aplicada, "fixada" quando temos somente a primeira derivada e "natural" quando temos a segunda derivada.

    Return:
        list: lista de listas.
    '''
    # Junta todas as sublistas das condições em uma unica lista
    coeficientes = condicoes.condicao_um(x) + condicoes.condicao_dois(x) + condicoes.condicao_tres(x)
    coeficientes += condicoes.condicao_quatro(x) + condicoes.condicao_cinco(x, condicao)
    
    return coeficientes

def termos_constantes(y:list, valores = [0,0])->list:
    '''
    Gerar a lista com termos constantes para solução do sistema linear que ira determinar as subfunções.
    
    Paramêtros:
        y (list): Lista com as ordenadas para determinar o spline.
        valores (list): Lista de dois elementos que definir os termos constantes das quinta condição

    Return:
        list: Uma lista com os termos constantes para solução.
    '''    
    #Lista com resultados não nulos
    termos_constantes = y[:-1]              # Coeficientes da primeira condição
    termos_constantes += y[1:]              # Coeficientes da segunda condição
    termos_constantes += [0]*(len(y) - 2)   # Coeficientes da Terceira condição
    termos_constantes += [0]*(len(y) - 2)   # Coeficientes da Quarta condição
    termos_constantes += valores            # Coeficientes da Quinta condição
    
    return termos_constantes

def resolver_gauss(A:list[list], b:list[float])->list[float]:
    """
    Resolve um sistema linear Ax = b usando o método de Eliminação de Gauss.
    
    Parâmetros:
        A (List[list]): Lista de listas (Matriz dos coeficientes)
        b (List[float]): Matriz dos termos independentes
    
    Retorno:
        List[float]: (solução do sistema)
    
    Exceções:
        ValueError: Caso a matriz seja singular ou as dimensões sejam inválidas.
    """

    # 1. Validação da existência da valores internos 
    if not A or not b:
        raise ValueError("Entrada inválida: Uma das matrizes ou ambas são vazias")
    # 2. Validação de Dimensões
    if len(A) != len(b):
        raise ValueError("Número de equações e variáveis são diferente, impossível determinar solução única.")
    # 3. Verificação da quadratura (N x N)
    for linha in A:
        if len(linha) != len(b):
            raise ValueError("A matriz não é quadrada (N x N).")
    
    M = [A[i] + [b[i]] for i in range(len(A))]  # Matriz Aumentada
    n_linhas = len(M)                           # Número de linha na matriz aumentada
    n_colunas = len(M[0])                       # Número de colunas na matriz aumentada

    # Criar a matriz triângula superior
    coluna = 0 # Indica a coluna que está sendo analisada
    for linha in range(n_linhas):

        # Caso o pivo seja zero, esse bloco tenta realizar a trocar de pivo alterando as posições das linhas
        if M[linha][linha] == 0:                                            
            for k in range(linha+1,n_linhas):
                if M[k][linha]!=0:
                    M[linha], M[k] = M[k], M[linha]
                    break
        
        # Caso a alteração anterior não tenha sindo possível o que indica que todos os elementos  
        # da coluna abaixo da linha <linha> são zero esse bloco força o pulor para linha seguinte
        if M[linha][linha] == 0:
            continue
        else:
            # Calcula o fator e altera o valores presente na linha i
            for i in range(linha+1,n_linhas):
                fator = M[i][coluna]/M[linha][linha]
                M[i] = [M[i][_] - fator*M[linha][_] for _ in range(n_colunas)]
        
        coluna += 1
    
    # Substituição Retroativa
    solucao = [0]*n_linhas
    for linha in range(n_linhas-1, -1, -1):
        soma = sum(M[linha][coluna]*solucao[coluna] for coluna in range(n_colunas-1))
        solucao[linha] = (M[linha][-1]-soma)/M[linha][linha]
        
    return solucao

def solucao(x: list, y: list, condicao = 'natural', valores = [0,0])-> list:
    '''
    Criar e resolver o sistema sistema linear (Ax=b) com os coeficientes de cada subfunção que compõem a spline
    
    Paramêtros:
        x (list): lista com abscissas dos diversos pontos.
        y (list): Lista com as ordenadas dos diversos pontos.
        condicao (str): Tipo de condição a se aplicada, "fixado" quando temos somente a primeira derivada e "natural" quando temos a segunda derivada.
        valores (list): Lista de dois elementos que definir os termos constantes das condições.

    Return:
        list: Lista de lista com os coeficientes associados a cada subfunção que compõem a spline.
                c[i,j] onde 0 <= i <= n-2 e 0 <= j <= 3 representa os coeficientes da subfunção i e coeficiente
                j da equação do terceiro grau.
    '''
    
    A = matriz_dos_coeficientes(x, condicao)    # Matriz dos coeficientes
    b = termos_constantes(y, valores)           # Matriz dos termos independentes

    # Agrupado os coeficientes de acordo com subfunção s_i
    coeficientes = []
    k = []
    count = 1
    for i in resolver_gauss(A, b):
        
        k.append(float(i))
        count += 1
        
        if count > 4:
            coeficientes.append(k)
            k = []      # Reinicializa a lista
            count = 1   # Reinicia a contagem
    
    # Adiciona o último conjunto se não estiver vazio
    if k:
        coeficientes.append(k)

    return coeficientes