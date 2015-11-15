import sys
import math
import timeit
import random


class Question(object):

    def __init__(self,nx,mx):
        self.n = nx
        self.m = mx
        self.nodes = range(0,self.n)
        self.node_ids = self.nodes

   

    def HizliBul_Bul(self,node1, node2):
        return self.node_ids[node1] == self.node_ids[node2]


    def HizliBul_Birlestir(self,node1,node2):
        eskiId = self.node_ids[node1]
        for x in self.nodes:
            if self.node_ids[x] == eskiId:
                self.node_ids[x] = self. node_ids[node2]

    def HizliBirlesim_Bul(self,node1,node2):
        return self.HizliBirlesim_KokBul(node1) == self.HizliBirlesim_KokBul(node2)
        
    
    def HizliBirlesim_KokBul(self,node):
        while(node != self.node_ids[node]):
            node = self.node_ids[node]
        return node

    def HizliBirlesim_Birlestir(self,node1,node2):
        node1_kok = self.HizliBirlesim_KokBul(node1)
        node2_kok = self. HizliBirlesim_KokBul(node2)
        self.node_ids[node2_kok] = node1_kok

    def AgirlikliHizliBirlesim_KokBul(self,node):
        while(node != self.node_ids[node]):
            node = self.node_ids[node]
        return node    

    def AgirlikliHizliBirlesim_Derinlik(self,node):
        sayac = 0
        while(node != self.node_ids[node]):
            sayac+=1
            node = self.node_ids[node]
        return sayac


    def AgirlikliHizliBirlesim_Bul(self, node1,node2):
        return self.AgirlikliHizliBirlesim_KokBul(node1) == self.AgirlikliHizliBirlesim_KokBul(node2)
        

    def AgirlikHizliBirlesim_Birlestir(self,node1,node2):
        node1_kok = self.node_ids[node1]
        node2_kok = self.node_ids[node2]
        d1 = self.AgirlikliHizliBirlesim_Derinlik(node1)
        d2 = self.AgirlikliHizliBirlesim_Derinlik(node2)
        if d1 > d2:
            self.node_ids[node2] = node1_kok
        else:
            self.node_ids[node1] = node2_kok

    def PatikaSikistirma_Kokbul(self,node):
        toTheTop = []       
        while(node != self.node_ids[node]):
            toTheTop.append(node)
            node = self.node_ids[node]        
        for x in toTheTop:
            self.node_ids[x] = node




    def PatikaSikistirma_Bul(self,node1,node2):
       return self.PatikaSikistirma_Kokbul(node1) == self.PatikaSikistirma_Kokbul(node2)


    def PatikaSikistirma_Birlestir(self,node1,node2):
        node1_kok = self.node_ids[node1]
        node2_kok = self.node_ids[node2]
        d1 = self.PatikaSikistirma_Derinlik(node1)
        d2 = self.PatikaSikistirma_Derinlik(node2)
        if d1 > d2:
           self. node_ids[node2] = node1_kok
        else:
            self.node_ids[node1] = node2_kok

    def PatikaSikistirma_Derinlik(self,node):
        sayac = 0
        while(node != self.node_ids[node]):
            sayac+=1
            node = self.node_ids[node]
        return sayac
    



def main():

    zamanlar = {}

    n = random.randint(1000,2000)
    m = random.randint(n / 2,n - 1)
    qHizliBul = Question(n,m)
    qHizliBirlesim = Question(n,m)
    qAgirlikli = Question(n,m)
    qPatika = Question(n,m)
    hizliBul_zamanlar = []
    hizliBirlesim_zamanlar = []
    hizliBirlesimAgirlikli_zamanlar = []
    patikaSikistirma_zamanlar = []

    for x in range(1,qHizliBul.m):

        n1 = qHizliBul.nodes[random.randint(0,n - 1)]
        n2 = qHizliBul.nodes[random.randint(0,n - 1)]
        while(n1 == n2 or qHizliBul.node_ids[n1] == qHizliBul.node_ids[n2]):
            n1 = qHizliBul.nodes[random.randint(0,n - 1)]
            n2 = qHizliBul.nodes[random.randint(0,n - 1)]
        s = timeit.default_timer()
        qHizliBul.HizliBul_Birlestir(n1,n2)
        hizliBul_zamanlar.append(timeit.default_timer() - s)
        pass

    zamanlar["hb"] = hizliBul_zamanlar

    for x in range(1,qHizliBirlesim.m):
        n1 = qHizliBirlesim.nodes[random.randint(0,n - 1)]
        n2 = qHizliBirlesim.nodes[random.randint(0,n - 1)]
        while(n1 == n2 or qHizliBirlesim.HizliBirlesim_KokBul(n1) == qHizliBirlesim.HizliBirlesim_KokBul(n2)):            
            n1 = qHizliBirlesim.nodes[random.randint(0,n - 1)]
            n2 = qHizliBirlesim.nodes[random.randint(0,n - 1)]
        s = timeit.default_timer()
        qHizliBirlesim.HizliBirlesim_Birlestir(n1,n2)
        hizliBirlesim_zamanlar.append(timeit.default_timer() - s)

    
    zamanlar["hbir"] = hizliBul_zamanlar

    for x in range(1,qAgirlikli):
        n1 = qAgirlikli.nodes[random.randint(0,n - 1)]
        n2 = qAgirlikli.nodes[random.randint(0,n - 1)]
        while(n1 == n2 or qAgirlikli.AgirlikliHizliBirlesim_KokBul(n1) == qAgirlikli.AgirlikliHizliBirlesim_KokBul(n2)):
            n1 = qAgirlikli.nodes[random.randint(0,n - 1)]
            n2 = qAgirlikli.nodes[random.randint(0,n - 1)]
        s = timeit.default_timer()
        qAgirlikli.AgirlikHizliBirlesim_Birlestir(n1,n2)
        hizliBirlesimAgirlikli_zamanlar.append(timeit.default_timer() - s)

    
    zamanlar["ahb"] = hizliBirlesimAgirlikli_zamanlar







    input()
    #for x in range(1,qHizliBirlesim):
        
    #    pass
if __name__ == "__main__":
    sys.exit(int(main() or 0))

