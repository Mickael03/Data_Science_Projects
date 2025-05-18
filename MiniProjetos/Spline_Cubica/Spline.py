import SistemaEquacoes

class SplineCubica():
    '''
    Classe para representar uma spline cúbica.
    
    Parâmetros:
        x (list): Lista com abscissas dos pontos de interpolação.
        y (list): Lista com as ordenadas dos pontos de interpolação.
        condicao (str, opcional): Defini a condição de fronteira a se aplicada. 'natural' ou 'fixado'.
        valores (list, opcional): Lista com dois elementos que definem os termos constantes da condição de fronteira.
    '''

    def __init__(self, x, y, condicao = 'natural', valores = [0,0]):
        '''Inicializa a classe SplineCubica com os pontos de interpolação e a condição de fronteira.'''
        
        if not (isinstance(x, list) and isinstance(y, list)): # Verifica se x e y são listas
            raise TypeError("x e y devem ser listas.")
        if len(x) != len(y): # Verificar se x e y têm o mesmo tamanho
            raise ValueError("x e y devem ter o mesmo tamanho.")
        
        self.x = x
        self.y = y
        self.condicao = condicao
        self.valores = valores
        self.coeficientes = SistemaEquacoes.solucao(x, y, condicao, valores)

    def __valor(self, numero):
        '''Calcula o valor da spline cúbica para um determinado ponto.
        
        Parâmetro:
            numero (float): Número que se deseja calcula o valor do spline
        
        Returno:
            float: Retorna o valor calculado do spline.
        '''

        for i in range(len(self.x)-1):
            if self.x[i] <= numero <= self.x[i+1]:
                c_0 = self.coeficientes[i][0]
                c_1 = self.coeficientes[i][1]
                c_2 = self.coeficientes[i][2]
                c_3 = self.coeficientes[i][3]

                return c_0 + c_1*(numero - self.x[i]) + c_2*(numero - self.x[i])**2 + c_3*(numero - self.x[i])**3
            
    def __lista_valores(self, lista):
        '''Calcula os valores da spline cúbica para uma lista de pontos.
        
        Parâmetro:
            lista (list): lista de valores que se deseja calcula o valor do spline
            
        Returne:
            list: Retorna uma lista com os valores calculados do spline
        '''

        return [self.__valor(i) for i in lista]
 

    def __call__(self, numero):
        '''
        Dar a classe um comportamento de função.
        
        Parâmetros:
            numero (float ou list): Ponto ou lista de pontos onde se deseja calcular o valor da spline.
            
        Retorno:
            float or list:  valor da spline cúbica no ponto especificado.
        '''

        if isinstance(numero, list):
            return self.__lista_valores(numero)
        if isinstance(numero, (int,float)):
            return self.__valor(numero)