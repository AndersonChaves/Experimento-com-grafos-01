import networkx as nx
import numpy
import os

class ConversorDeArquivos:
  def _linhaVazia(self, linha):
    return (linha == '' or linha == '\n')

  def _linhaETituloDoGrafo(self, linha):
    return ('a' in linha)

  def _lerMatrizesNauty(self, arquivo):
    listaDeMatrizes = []
    i = -1
    for linha in arquivo:
      if not (self._linhaVazia(linha)):
        if self._linhaETituloDoGrafo(linha):
          listaDeMatrizes.append([])
          i = i + 1
        else:
          listaDeMatrizes[i].append(map(int, linha.split(' ')))
    return listaDeMatrizes

  def _converterMatrizDeAdjacenciaParaGrafo(self, matrizDeAdjacencia):
    return nx.from_numpy_matrix(numpy.matrix(matrizDeAdjacencia))

  def _escreverGrafosEmArquivosGraphML(self, listaDeGrafos, caminho):
    for i in range(len(listaDeGrafos)):
      arquivo_de_saida = open(caminho + "\\" + str(i + 1) + ".txt", "w")
      nx.write_graphml(listaDeGrafos[i], arquivo_de_saida)

  def converterArquivoNautyParaGraphML(self, caminhoDoArquivoDeEntrada, caminhoDosArquivosDeSaida):
    arquivo = open(caminhoDoArquivoDeEntrada, 'r')
    listaDeMatrizes = self._lerMatrizesNauty(arquivo)
    listaDeGrafos = []
    for matriz in listaDeMatrizes:
      listaDeGrafos.append(self._converterMatrizDeAdjacenciaParaGrafo(matriz))
    self._escreverGrafosEmArquivosGraphML(listaDeGrafos, caminhoDosArquivosDeSaida)

  def converterGrafosNautyParaGraphML(self, caminhoDasAmostras):
    for arquivo in os.listdir(caminhoDasAmostras):
      nomeDoArquivo, extensao = os.path.splitext(arquivo.title())
      if extensao.lower() == ".txt":
        nomeDoDiretorioASerEscrito = caminhoDasAmostras + "\\" + nomeDoArquivo
        if not os.path.exists(nomeDoDiretorioASerEscrito):
          os.makedirs(nomeDoDiretorioASerEscrito)
        self.converterArquivoNautyParaGraphML(caminhoDasAmostras + arquivo.title())