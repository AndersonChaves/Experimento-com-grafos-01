import networkx as nx
import numpy

def calcularVetorFiedlerNetworkx(grafo):
  return nx.fiedler_vector(grafo)


def posicaoDoSegundoMenorValorEmLista(listaDeNumeros):
    menorValor, segundoMenorValor = float('inf'), float('inf')
    p1 = 0
    p2 = 0
    for i in range(len(listaDeNumeros)):
        if listaDeNumeros[i] <= menorValor:
            menorValor, segundoMenorValor = listaDeNumeros[i], menorValor
            p1, p2 = i, p1
        elif listaDeNumeros[i] < segundoMenorValor:
            segundoMenorValor = listaDeNumeros[i]
            p2 = i
    return p2

def calcularVetorFiedlerNumpy(grafo):
    eigenvalues, eigenvectors = numpy.linalg.eig(nx.laplacian_matrix(grafo).A)
    posicaoVetor = posicaoDoSegundoMenorValorEmLista(eigenvalues)
    vetorFiedler = eigenvectors[:, posicaoVetor]
    for i in range(len(vetorFiedler)):
        vetorFiedler[i] = round(vetorFiedler[i], 8)
    return vetorFiedler

def calcularVetoresFiedler(listaDeGrafos):
  F = []
  for grafo in listaDeGrafos:
    f = calcularVetorFiedlerNumpy(grafo)
    F.append(f)
  return F
