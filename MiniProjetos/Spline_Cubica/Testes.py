from Spline import SplineCubica
import unittest

class TestNatural(unittest.TestCase):

    def test_DoisPontos(self):

        with self.subTest(msg = 'Dois pontos, sub teste 1'):
            spline = SplineCubica([-3, 0],[0, 7],'natural')
            esperado = [[0.0, 2.3333333333333335, 0.0, 0.0]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente") #Verificar o número de equações
            for i in range(len(esperado)): #Verificar a quantidade de coeficientes para determinada equação
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])): #Comparar cada um dos coeficientes
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Dois pontos, sub teste 2'):
            spline = SplineCubica([-3, 0],[0, 7],'natural', valores=[-0.8, 4.9])
            esperado = [[0.0, 0.6833333333333341, -0.4, 0.3166666666666666]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

    def test_TresPontos(self):

        with self.subTest(msg = 'Três pontos, sub teste 1'):
            spline = SplineCubica([-3, 0, 2], [0, 7, 4], 'natural')
            esperado = [[0.0, 3.483333333333333, 4.440892098500626e-16, -0.12777777777777785],
                        [7.0, 0.03333333333333341, -1.15, 0.19166666666666665]
                        ]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Três pontos, sub teste 2'):
            spline = SplineCubica([-3, 0, 2], [0, 7, 4], 'natural', valores=[7.1,-3.4])
            esperado = [[0.0, -2.891666666666667, 3.5500000000000007, -0.6027777777777779],
                        [7.0, 2.1333333333333337, -1.8750000000000004, 0.029166666666666785]
                        ]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

    def test_QuatroPontos(self):

        with self.subTest(msg = 'Quatro pontos, sub teste 1'):
            spline = SplineCubica([-3, 0, 2, 5], [0, 7, 4, 1], 'natural')
            esperado = [[0.0, 3.5625, 1.6653345369377348e-16, -0.1365740740740741],
                        [7.0, -0.1249999999999998, -1.2291666666666667, 0.2708333333333333],
                        [4.0, -1.791666666666667, 0.3958333333333335, -0.0439814814814815]
                        ]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Quatro pontos, sub teste 2'):
            spline = SplineCubica([-3, 0, 2, 5], [0, 7, 4, 1], 'natural', valores=[5.7, -6.9])
            esperado = [[0.0, -1.0312500000000004, 2.85, -0.5761574074074074],
                        [7.0, 0.5125000000000002, -2.335416666666667, 0.6645833333333334],
                        [4.0, -0.8541666666666666, 1.6520833333333333, -0.5668981481481482]
                        ]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

class TestFixados(unittest.TestCase):

    def test_DoisPontos(self):

        with self.subTest(msg = 'Dois pontos, sub teste 1'):
            spline = SplineCubica([0, 5], [7, 1], 'fixado')
            esperado = [[7.0, 0.0, -0.72, 0.096]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Dois pontos, sub teste 2'):
            spline = SplineCubica([0, 5], [7, 1], 'fixado', valores=[-5, 7])
            esperado = [[7.0, -5.0, -0.1200000000000001, 0.17600000000000002]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

    def test_TresPontos(self):

        with self.subTest(msg = 'Três pontos, sub teste 1'):
            spline = SplineCubica([-5,0,10], [7, 1, 4], 'fixado')
            esperado = [[7.0, 0.0, -0.51, 0.05399999999999999],
                        [1.0, -1.05, 0.3, -0.016499999999999997]
                        ]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Três pontos, sub teste 2'):
            spline = SplineCubica([-5,0,1], [-3,-1,5], 'fixado', valores=[1.5, -5.2])
            esperado = [[-3.0, 1.5, -2.288333333333333, 0.41366666666666657],
                        [-1.0, 9.641666666666666, 3.9166666666666687, -7.5583333333333345]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

    def test_QuatroPontos(self):
        
        with self.subTest(msg = 'Quatro pontos, sub teste 1'):
            spline = SplineCubica([-6,-4,0,3], [4,2,10,0], 'fixado')
            esperado = [[4.0, 0.0, -1.6358024691358024, 0.5679012345679012],
                        [2.0, 0.2716049382716049, 1.7716049382716048, -0.33487654320987653],
                        [10.0, -1.6296296296296295, -2.246913580246914, 0.5596707818930041]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

        with self.subTest(msg = 'Quatro pontos, sub teste 2'):
            spline = SplineCubica([-6,-4,-1,0], [4,2,10,0], 'fixado', valores=[-10,10])
            esperado = [[4.0, -10.000000000000002, 5.166666666666668, -0.3333333333333337],
                        [2.0, 6.666666666666667, 3.166666666666667, -1.5],
                        [10.0, -14.833333333333334, -10.333333333333332, 15.166666666666666]]
            self.assertEqual(len(spline.coeficientes), len(esperado), "Número de linhas com os coeficientes são diferente")
            for i in range(len(esperado)):
                self.assertEqual(len(spline.coeficientes[i]), len(esperado[i]), f"Números de coeficientes na linha {i} são diferentes")
                for j in range(len(esperado[i])):
                    self.assertAlmostEqual(spline.coeficientes[i][j], esperado[i][j], places=7, msg=f"Divergência no coeficiente [{i}][{j}]")

unittest.main()