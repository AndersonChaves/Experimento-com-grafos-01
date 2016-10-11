from LeituraDeArquivos import ConversorDeArquivos
from LeitorDeGrafos import LeitorDeGrafos
from DesenhoDeGrafos import DesenhistaDeGrafos
import CalculoDeVetores as calc
import os
import networkx as nx
import numpy

def lerArquivoDeConfiguracoes(caminhoDoArquivoDeConfiguracoes):
    arquivo = open(caminhoDoArquivoDeConfiguracoes)
    config = {}
    for line in arquivo:
        line = line.replace('\n', '')
        (chave, valor) = line.split(':')
        config[chave] = valor
    return config

def lerConfiguracoes():
  return lerArquivoDeConfiguracoes("config.txt")

def verificarConversaoDeArquivos(configuracoes):
  if configuracoes["converter_grafos"] == 'S':
    conversor = ConversorDeArquivos()
    conversor.converterGrafosNautyParaGraphML("Amostras\Matrizes de Adjacencia\\")

def obterListaDeTiposDeGrafos(configuracoes):
  return configuracoes["tipos_dos_grafos"].replace(' ', '').split(',')

def lerGrafosGraphML(tipoDeGrafo):
  leitorDeGrafos = LeitorDeGrafos()
  listaDeGrafos = leitorDeGrafos.lerGrafosGraphML("Amostras\GraphML\\", tipoDeGrafo)
  return listaDeGrafos

def desenharGrafos(listaDeGrafos, F, nomeDaPasta):
  desenhista = DesenhistaDeGrafos()
  caminhoParaSalvar = "Amostras\Graficos\\" + nomeDaPasta
  if not os.path.exists(caminhoParaSalvar):
      os.makedirs(caminhoParaSalvar)
  for i in range(len(listaDeGrafos)):
      nomeDoArquivo = caminhoParaSalvar + "\\" + str(i+1) + ".png"
      desenhista.plotarGrafoDeAcordoComVetorFiedler(listaDeGrafos[i], F[i], nomeDoArquivo)

def escreverVetoresFiedler(F, diretorio, nomeDoArquivo):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    arquivo = open(diretorio + "\\" + nomeDoArquivo, "w")
    for i in range(len(F)):
        arquivo.write("Vetor Fiedler do grafo: " + str(i + 1) + "\n")
        arquivo.write(str(F[i]))
        arquivo.write("\n\n")

def escreverMatrizLaplaciana(listaDeGrafos, diretorio, nomeDoArquivo):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    arquivo = open(diretorio + "\\" + nomeDoArquivo, "w")
    i = 0
    for grafo in listaDeGrafos:
        laplaciana = nx.laplacian_matrix(grafo).A
        arquivo.write("Matriz Laplaciana do grafo: " + str(i + 1) + "\n")
        arquivo.write(str(laplaciana))

        arquivo.write("\n\nAutovalores: \n")
        eigenvalues, _ = numpy.linalg.eig(laplaciana)
        arquivo.write(str(eigenvalues))
        arquivo.write("\n\n\n")
        i = i + 1

if __name__ == "__main__":
    configuracoes = lerConfiguracoes()
    verificarConversaoDeArquivos(configuracoes)
    tiposDeGrafos = obterListaDeTiposDeGrafos(configuracoes)

    for tipoDeGrafo in tiposDeGrafos:
        listaDeGrafos = lerGrafosGraphML(tipoDeGrafo)
        F = calc.calcularVetoresFiedler(listaDeGrafos)
        if configuracoes["desenhar_grafos"].strip() == 'S':
          desenharGrafos(listaDeGrafos, F, tipoDeGrafo)
        if configuracoes["escrever_vetores_fiedler"].strip() == 'S':
          escreverVetoresFiedler(F, "Vetores Fiedler", tipoDeGrafo + ".txt")
        if configuracoes["escrever_laplaciana"].strip() == 'S':
          escreverMatrizLaplaciana(listaDeGrafos, "Laplacianas", tipoDeGrafo + ".txt")



