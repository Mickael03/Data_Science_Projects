from numpy.linalg import solve
import Condicoes

def matriz_dos_coeficientes(x = [], condicao = 'natural'):
    '''
    Combina os coeficientes gerados pelas funções de condições para a montagem a matriz dos coeficientes para solucionar o sistema linear afim 
    de determinar os coeficientes de cada subfunção.
    
    Paramêtros:
        x (list): Lista das abscissas dos pontos para determinar a spline.
        condicao (str): Tipo de condição a se aplicada, "fixada" quando temos somente a primeira derivada e "natural" quando temos a segunda derivada.

    Return:
        list: Uma lista de listas.
    '''
    # Junta todas as sublistas das condições em uma unica lista
    coeficientes = Condicoes.condicao_um(x) + Condicoes.condicao_dois(x) + Condicoes.condicao_tres(x)
    coeficientes += Condicoes.condicao_quatro(x) + Condicoes.condicao_cinco(x, condicao)
    
    return coeficientes

def termos_constantes(y = [], valores = [0,0]):
    '''
    Gerar a lista com termos constantes para solução do sistema linear que ira determinar as subfunções.
    
    Paramêtros:
        y: Lista com as ordenadas para determinar o spline.
        valores (list): Lista de dois elementos que definir os termos constantes das quinta condição

    Return:
        list: Uma lista com os termos constantes para solução.
    '''    
    #Lista com resultados não nulos
    termos_constantes = y[:-1] # Coeficientes da primeira condição
    termos_constantes += y[1:] # Coeficientes da segunda condição
    termos_constantes += [0]*(len(y) - 2) # Coeficientes da Terceira condição
    termos_constantes += [0]*(len(y) - 2) # Coeficientes da Quarta condição
    termos_constantes += valores # Coeficientes da Quinta condição
    
    return termos_constantes

def solucao(x = [], y = [], condicao = 'natural', valores = [0,0]):
    '''
    Resolve o sistema linear Ax=b que determinar os coeficientes de cada subfunção que compõem a spline
    
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
    #Matriz dos coeficientes
    A = matriz_dos_coeficientes(x, condicao)
    
    #Matriz dos termos independentes
    b = termos_constantes(y, valores)

    # Agrupado os coeficientes de acordo com subfunção s_i
    coeficientes = []
    k = []
    count = 1
    for i in solve(A, b):
        
        k.append(float(i))
        count += 1
        
        if count > 4:
            coeficientes.append(k)
            k = []  # Reinicializa a lista
            count = 1  # Reinicia a contagem
    
    # Adiciona o último conjunto se não estiver vazio
    if k:
        coeficientes.append(k)

    return coeficientes