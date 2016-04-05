# encoding:utf8
# qpy:console
#
# programa ilustrando o uso de grafos
#
# EM ADAPTÁCÃO PARA FAZER BUSCA

import os


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
            print "Destino: {}  índice {} ".format(
                grf.verticeRotulo(grf.indiceDestino), grf.indiceDestino)
            print

    def localizaRotulo(self, rotulo):
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo):
                return i
        return -1


class Buscador:
    def __init__(self, grf):
        self.proximos = []
        self.visitados = []
        self.grf = grf
        self.destino = grf.indiceDestino

    def clean(self):
        if self.proximos:
            self.proximos = []
        if self.visitados:
            self.visitados = []

    def expandirProximos(self, vertice):
        for vAdjacente in range(self.grf.numVertices):
            if self.grf.matrizAdjacencias[vertice][vAdjacente]:
                if vAdjacente not in self.visitados:
                    if vAdjacente not in self.proximos:
                        self.proximos.append(vAdjacente)

    def imprimeLista(self, lista):
        print "##############################\n\n"
        print "Tamanho lista visitados: ", len(lista)
        print "Caminho percorrido: "

        for i in range(len(lista)):
            print self.grf.verticeRotulo(self.visitados[i]),
        print "\n\n##############################"

    def bLargura(self):
        if self.proximos:
            self.clean()
        # Colocando raiz na fila
        self.proximos.append(self.grf.indiceOrigem)

        while self.proximos:
            verticeAtual = self.proximos.pop(0)
            self.visitados.append(verticeAtual)

            if verticeAtual == self.destino:
                print "Vertice Destino {}".format(
                    self.grf.verticeRotulo(verticeAtual)), "Encontrado"

                self.imprimeLista(self.visitados)
                return True

            # Expandir para o proximo nível.
            self.expandirProximos(verticeAtual)

    def adjacentes(self, vertice):
        adjacentes = []
        for i, val in enumerate(self.grf.matrizAdjacencias[vertice]):
            if self.grf.matrizAdjacencias[vertice][i]:
                adjacentes.append(i)
        return adjacentes

    def bProfundidade(self, verticeAtual):
        self.visitados.append(verticeAtual)
        if verticeAtual == self.destino:
            print "Vertice Destino {}".format(
                self.grf.verticeRotulo(verticeAtual)), "Encontrado"
            self.imprimeLista(self.visitados)
            return True

        for adj in self.adjacentes(verticeAtual):
            if adj not in self.visitados:
                self.bProfundidade(adj)

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
            buscador.clean()
            buscador.bLargura()

        elif escolha == 'p':
            print
            print "Busca por Profundidade"
            buscador = Buscador(grf)
            buscador.clean()
            buscador.bProfundidade(grf.indiceOrigem)

        elif escolha == 's':
            break
        else:
            print "Entrada inválida Pressione Enter "
            raw_input()
