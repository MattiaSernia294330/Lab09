import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._lista_nodi=[]
        self._lista_edge=[]
        self._dizionario={}
        self._numero={}
        self._nodi={}

    def handleAnalizza(self,distanza):
        pass
    def creaGrafo(self,distanza):
        self._grafo.clear()
        lista_nodi=DAO._getAereoporti()
        for nodi in lista_nodi:
            self._dizionario[nodi.ID]=nodi
        listina=DAO._getLinea()
        for linea in listina:
            if f"{linea.ORIGIN_AIRPORT_ID}-{linea.DESTINATION_AIRPORT_ID}" in self._nodi or f"{linea.DESTINATION_AIRPORT_ID}-{linea.ORIGIN_AIRPORT_ID}" in self._nodi:
                chiave=""
                for key in self._nodi:
                     if f"{linea.ORIGIN_AIRPORT_ID}-{linea.DESTINATION_AIRPORT_ID}"==key or f"{linea.DESTINATION_AIRPORT_ID}-{linea.ORIGIN_AIRPORT_ID}"==key:
                        chiave=key
                        break
                alfa=self._nodi[chiave]*self._numero[chiave]
                self._numero[chiave]+=1
                self._nodi[chiave]=(alfa+linea.DISTANCE)/self._numero[chiave]
            else:
                self._nodi[f"{linea.ORIGIN_AIRPORT_ID}-{linea.DESTINATION_AIRPORT_ID}"]=linea.DISTANCE
                self._numero[f"{linea.ORIGIN_AIRPORT_ID}-{linea.DESTINATION_AIRPORT_ID}"]=1
        self.creaEdges(distanza)
        for element in self._lista_edge:
            self._grafo.add_edge(self._dizionario[element.split("-")[0]],self._dizionario[element.split("-")[1]],distanza=self._nodi[element])

    def creaEdges(self,distanza):
        for nodi in self._nodi:
            if self._nodi[nodi]>=distanza:
                self._lista_edge.append(nodi)


    def numNodi(self):
        return len(self._lista_nodi)
    def Edge(self):
        lista_distanze=[]
        for element in self._lista_edge:
            lista_distanze.append(self._nodi[element])
        return self._lista_edge,lista_distanze,len(self._lista_edge)










