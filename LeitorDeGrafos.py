import networkx as nx
import os

class LeitorDeGrafos:

  def _reordenarGrafo(self, grafo):
    mapping = {}
    for i in range(grafo.order()):
      mapping[str(i)] = i
    grafo = nx.relabel_nodes(grafo, mapping)
    return grafo

  def lerGrafo(self, diretorio):
    grafoGraphML = nx.read_graphml(diretorio)
    grafoGraphML = self._reordenarGrafo(grafoGraphML) #Necessario para preservar a ordem da matriz
    return grafoGraphML

  def lerGrafosGraphML(self, diretorioPai, tipoDeGrafo):
    G = []
    diretorioDosGrafos = (diretorioPai + tipoDeGrafo + "\\")
    for i in range(len(os.listdir(diretorioDosGrafos))):
      grafo = self.lerGrafo(diretorioDosGrafos + str(i+1) + ".txt")
      G.append(grafo)
    return G