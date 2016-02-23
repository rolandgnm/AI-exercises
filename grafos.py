#encoding:utf8
#qpy:console
#
# programa ilustrando o uso de grafos
#
#
import os
class Vertice:
    def __init__(self,rotulo):
        self.rotulo = rotulo
    def igualA(self,r):
        return r == self.rotulo
 
class Grafo:
    def __init__(self):
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz=[]
            for j in range(self.numVerticesMaximo): 
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)
 
    def adicionaVertice(self,rotulo):
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))
     
    def adicionaArco(self,inicio,fim):
        self.matrizAdjacencias[inicio][fim] = 1
        self.matrizAdjacencias[fim][inicio] = 1
         
 
    #def mostraVertice(self,vertice):
    #   print self.matrizAdjacencias[vertice].rotulo
         
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
    def localizaRotulo(self,rotulo):
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo): return i
        return -1           
         
if __name__== "__main__":
    os.system("clear")    
    grf=Grafo()
    while True:
        print "Escolha sua opção "
        print "(M) mostra, (V) inserir Vértice  (A) Inserir Arco (S) sair"
        escolha = str(raw_input("Digite sua opção ")).lower()
        if escolha == 'm':
            grf.imprimeMatriz()
        elif escolha == 'v':
            val = str(raw_input("Digite o rótulo do arco  a inserir "))            
            grf.adicionaVertice(val)
        elif escolha == 'a':
            rinicio = str(raw_input("Digite o rótulo do vértice de início do arco "))
            inicio = grf.localizaRotulo(rinicio)
            if inicio == -1 : 
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            rfim = str(raw_input("Digite o rótulo do vértice de fim do arco "))            
            fim = grf.localizaRotulo(rfim)
            if fim == -1 : 
                print "Vértice não cadastrado. Cadastre o vértice primeiro "
                raw_input()
                continue
            grf.adicionaArco(inicio, fim) 
        elif escolha == 's':
            break
        else:
            print "Entrada inválida Pressione Enter "
            raw_input()