import networkx as nx
import matplotlib.pyplot as plt

class DesenhistaDeGrafos:
    def plotarGrafo(self, G):
        pos = nx.spring_layout(G)
        print pos
        nx.draw_networkx_nodes(G, pos,
                               node_color='b',
                               node_size=500,
                               alpha=0.8)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
        labels = {}
        for node in G.nodes():
            labels[node] = str(node)
        nx.draw_networkx_labels(G, pos, labels, font_size=10)
        plt.show()
        plt.clf()

    def plotarGrafoDeAcordoComVetorFiedler(self, grafo, vetorFiedler, diretorio):
        verticesPositivos = []
        verticesNegativos = []
        for i in range(len(vetorFiedler)):
            if vetorFiedler[i] >= 0:
                verticesPositivos.append(grafo.nodes()[i])
            else:
                verticesNegativos.append(grafo.nodes()[i])


        if grafo.order() <= 40:
           tamanhoDoNo = 750
           tamanhoDaFonte = 15
        elif grafo.order() <= 60:
            tamanhoDoNo = 400
            tamanhoDaFonte = 12
        elif grafo.order() <= 100:
            tamanhoDoNo = 100
            tamanhoDaFonte = 8


        pos = nx.circular_layout(grafo)
        nx.draw_networkx_nodes(grafo, pos, verticesPositivos,
                               node_color='r',
                               node_size=tamanhoDoNo,
                               alpha=0.8)
        nx.draw_networkx_nodes(grafo, pos, verticesNegativos,
                               node_color='b',
                               node_size=tamanhoDoNo,
                               alpha=0.8)


        nx.draw_networkx_edges(grafo, pos, width=1.0, alpha=0.5)
        labels = {}
        for node in grafo.nodes():
            labels[node] = str(node)
        nx.draw_networkx_labels(grafo, pos, labels, font_size=tamanhoDaFonte)
        plt.axis('off')
        plt.savefig(diretorio)
        plt.clf()




