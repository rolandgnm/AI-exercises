# encoding:utf8
# qpy:console
#
# programa ilustrando o uso de grafos
#
# EM ADAPTÁCÃO PARA FAZER BUSCA

import os
from Queue import Queue
from Queue import LifoQueue


class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo

    def igualA(self, r):
        return r == self.rotulo


class Grafo:
    def __init__(self):
        self.indiceDestino = None
        self.indiceOrigem = None
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz = []
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)

    def adicionaVertice(self, rotulo):
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))

    def adicionaArco(self, inicio, fim):
        self.matrizAdjacencias[inicio][fim] = 1
        self.matrizAdjacencias[fim][inicio] = 1

    def marcaInicio(self, indiceOrigem):
        self.indiceOrigem = self.localizaRotulo(indiceOrigem)

    def marcaDestino(self, indiceDestino):
        self.indiceDestino = self.localizaRotulo(indiceDestino)

    def verticeRotulo(self, indice):
        return self.listaVertices[indice].rotulo

    def imprimeMatriz(self):
        print " ",
        for i in range(self.numVertices):
            print self.listaVertices[i].rotulo,
        print
        for i in range(self.numVertices):
            print self.listaVertices[i].rotulo,
            for j in range(self.numVertices):
                print self.matrizAdjacencias[i][j],
            print

    def imprimeOrigemDestino(self):
        if grf.indiceOrigem is not None and grf.indiceDestino is not None:
            print "Origem: {}  índice {} ".format(
                grf.verticeRotulo(grf.indiceOrigem), grf.indiceOrigem)
            print "Destino:{}  índice {} ".format(
                grf.verticeRotulo(grf.indiceDestino), grf.indiceDestino)
            print

    def localizaRotulo(self, rotulo):
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo):
                return i
        return -1


class Buscador:
    def __init__(self, grf):
        self.fifo = Queue()
        self.lifo = LifoQueue()
        self.visitados = []
        self.grf = grf
        self.destino = grf.indiceDestino

    def clean(self):
        self.fifo = Queue()
        self.lifo = LifoQueue()
        self.visitados = []

    def imprimeLista(self, lista):
        for i in range(len(lista)):
            print self.grf.verticeRotulo(self.visitados[i]),

    def bLargura(self):
        # Colocando raiz na fila
        self.fifo.put(self.grf.indiceOrigem)

        while not self.fifo.empty():
            verticeAtual = self.fifo.get()
            self.visitados.append(verticeAtual)

            if verticeAtual == self.destino:
                print verticeAtual
                self.imprimeLista(self.visitados)
                return True

            # Expandir para o proximo nível.
            self.expandirFilaLargura(verticeAtual)

    def bProfundidade(self):
            # Colocando raiz na fila
            self.lifo.put(self.grf.indiceOrigem)

            while not self.lifo.empty():
                verticeAtual = self.lifo.get()
                self.visitados.append(verticeAtual)

                if verticeAtual == self.destino:
                    print verticeAtual
                    self.imprimeLista(self.visitados)
                    return True

                # Expandir para o proximo nível.
                self.expandirFilaLargura(verticeAtual)
            return False

    def expandirFilaLargura(self, vertice):
        for vAdjacente in range(self.grf.numVertices):
            if self.grf.matrizAdjacencias[vertice][vAdjacente]:

                if int(vAdjacente) not in self.visitados:
                    self.fifo.put(vAdjacente)


if __name__ == "__main__":
    os.system("clear")
    grf = Grafo()
    while True:
        print " "
        print "Escolha sua opção "
        print "(V) inserir Vértice  (A) Inserir Arco"
        print "(O) Marcar Vertice Origem e Destino para a Busca"
        print "(M) mostra Matriz"
        print "(L) Busca em Largura (P) Busca em profundidade"
        print "(S) sair"
        escolha = str(raw_input("Digite sua opção \n")).lower()
        if escolha == 'm':
            grf.imprimeMatriz()
            print " "
            grf.imprimeOrigemDestino()

        elif escolha == 'v':
            val = str(
                raw_input("Digite o rótulo do vértice  a inserir ")).upper()
            if grf.localizaRotulo(val) >= 0:
                print "Vértice já existe, tente outra vez"
                raw_input()
                continue
            if not val:
                raw_input()
                continue
            grf.adicionaVertice(val)

        elif escolha == 'a':
            rinicio = str(
                raw_input(
                    "Digite o rótulo do vértice de início do arco ")).upper()
            inicio = grf.localizaRotulo(rinicio)
            if inicio == -1:
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            rfim = str(
                raw_input(
                    "Digite o rótulo do vértice de fim do arco ")).upper()
            fim = grf.localizaRotulo(rfim)
            if fim == -1:
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            grf.adicionaArco(inicio, fim)

        elif escolha == 'o':
            rOrigem = str(
                raw_input("Digite o rótulo do vértice Origem ")).upper()
            if grf.localizaRotulo(rOrigem) == -1:
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            grf.marcaInicio(rOrigem)
            # print grf.indiceOrigem

            rDestino = str(
                raw_input("Digite o rótulo do vértice Destino ")).upper()
            if grf.localizaRotulo(rDestino) == -1:
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            grf.marcaDestino(rDestino)

        elif escolha == 'l':
            print
            print "Busca por Largura"
            buscador = Buscador(grf)
            buscador.bLargura()

            print
            print "Busca por Profundidade"
            buscador.clean()
            buscador = Buscador(grf)
            buscador.bProfundidade()

        elif escolha == 's':
            break
        else:
            print "Entrada inválida Pressione Enter "
            raw_input()
