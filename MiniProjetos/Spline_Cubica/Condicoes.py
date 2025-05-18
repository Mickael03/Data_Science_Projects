def condicao_um (x = []):
    '''
    Gera os coeficientes da primeira condição para determinar as subfunções da spline.
    
    Parâmetros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
      
    Retorna:
        list: Uma lista de listas, onde cada sublista contém os coeficientes para montar a matriz de solução do sistema.
    '''
    # Numeros de equações
    quantidade_de_equacoes = len(x) - 1

    # Coeficientes
    coeficientes = []

    #Gerar os coeficientes de cada subfunção da função por parte
    j = 0
    for _ in range(quantidade_de_equacoes):
        k = [0 for _ in range(4*quantidade_de_equacoes)]
        k[j] = 1
        j += 4
        coeficientes.append(k)
        
    return coeficientes

def condicao_dois(x = []):
    '''
    Gera os coeficientes da segunda condição para determinar as subfunções da spline.
    
    Parâmetros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
      
    Retorna:
        list: Uma lista de listas, onde cada sublista contém os coeficientes para montar a matriz de solução do sistema.
    '''
    # Numeros de equações
    quantidade_de_equacoes = len(x) - 1

    # Coeficientes
    coeficientes = []
    
    #Gerar os coeficientes de cada subfunção da função por parte
    i,j = 0,0
    for _ in range(quantidade_de_equacoes):
        k = [0 for elemento in range(4*quantidade_de_equacoes)]
        k[j]  = 1
        k[j+1] = x[i+1] - x[i]
        k[j+2] = (x[i+1] - x[i])**2
        k[j+3] = (x[i+1] - x[i])**3
        coeficientes.append(k)
        j += 4
        i += 1

    return coeficientes

def condicao_tres(x = []):
    '''
    Gera os coeficientes da terceira condição para determinar as subfunções da spline.
    
    Parâmetros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
      
    Retorna:
        list: Uma lista de listas, onde cada sublista contém os coeficientes para montar a matriz de solução do sistema.
    '''
    # Numeros de equações
    quantidade_de_equacoes = len(x) - 1

    # Coeficientes
    coeficientes = []

    # Gerar os coeficientes de cada uma das primeira derivadas das subfunção da função por parte
    i,j = 0, 0
    for _ in range(quantidade_de_equacoes-1):
        k = [0 for i in range(4*quantidade_de_equacoes)]
        k[j + 1] = 1
        k[j + 2] = 2*(x[i+1]-x[i])
        k[j + 3] = 3*(x[i+1]-x[i])**2
        k[j + 5] = -1
        
        coeficientes.append(k)
        j += 4
        i += 1

    return coeficientes

def condicao_quatro(x = []):
    '''
    Gera os coeficientes da quarta condição para determinar as subfunções da spline.
    
    Parâmetros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
      
    Retorna:
        list: Uma lista de listas, onde cada sublista contém os coeficientes para montar a matriz de solução do sistema.
    '''
    # Numeros de equações
    quantidade_de_equacoes = len(x) - 1

    # Coeficientes
    coeficientes = []

    # Gerar os coeficientes de cada uma das primeira derivadas das subfunção da função por parte
    i,j = 0,0
    for _ in range(quantidade_de_equacoes-1):
        k = [0 for i in range(4*quantidade_de_equacoes)]
        k[j + 2] = 2
        k[j + 3] = 6*(x[i+1]-x[i])
        k[j + 6] = -2
        
        coeficientes.append(k)
        j += 4
        i += 1
        
    return coeficientes

def condicao_cinco(x = [], condicao = 'natural'):
    '''
    Gera os coeficientes da quinta condição para determinar as subfunções da spline.
    
    Parâmetros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
        condicao (str): Tipo de condição a se aplicada, fixada quando temos somente a primeira derivada e natural quando temos a segunda derivada.
      
    Retorna:
        list: Uma lista de listas, onde cada sublista contém os coeficientes para montar a matriz de solução do sistema.
    '''
    # Número de equações 
    quantidade_de_equacoes = len(x) - 1

    # Lista com os coeficientes 
    coeficientes = []

    # Criar a lista com os coeficientes de  cada subfunção
    if condicao == 'fixado':
        k = [0 for i in range(4*quantidade_de_equacoes)]
        k[1] = 1
        k[2] = 2*(x[0]-x[0])
        k[3] = 3*(x[0]-x[0])**2

        z = [0 for i in range(4*quantidade_de_equacoes)]
        z[-1] = 3*(x[-1]-x[-2])**2
        z[-2] = 2*(x[-1]-x[-2])
        z[-3] = 1
    
        coeficientes = [k,z]
    
    if condicao == 'natural':
        k = [0 for i in range(4*quantidade_de_equacoes)]
        k[2] = 2
        k[3] = 6*(x[0]-x[0])

        z = [0 for i in range(4*quantidade_de_equacoes)]
        z[-1] = 6*(x[-1]-x[-2])
        z[-2] = 2
    
        coeficientes = [k,z]

    return coeficientes