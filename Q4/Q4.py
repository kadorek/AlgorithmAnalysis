import sys
import math
import timeit
import random


def main():
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

    #for x in range(1,qHizliBirlesim):
        
    #    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))


class Question:

    def __init__(self,nx,mx):
        self.n = nx
        self.m = mx
        self.nodes = [].extend(range(1,self.n))
        self.node_ids = []

   

    def HizliBul_Bul(self,node1, node2):
        return node_ids[node1] == node_ids[node2]


    def HizliBul_Birlestir(self,node1,node2):
        eskiId = node_ids[node1]
        for x in nodes:
            if node_ids[x] == eskiId:
                node_ids[x] = node_ids[node2]

    def HizliBirlesim_Bul(self,node1,node2):
        return HizliBirlesim_KokBul(node1) == HizliBirlesim_KokBul(node2)
        
    
    def HizliBirlesim_KokBul(self,node):
        while(node != node_ids[node]):
            node = node_ids[node]
        return node

    def HizliBirlesim_Birlestir(self,node1,node2):
        node1_kok = HizliBirlesim_KokBul(node1)
        node2_kok = HizliBirlesim_KokBul(node2)
        node_ids[node2_kok] = node1_kok

    def AgirlikliHizliBirlesim_KokBul(self,node):
        while(node != node_ids[node]):
            node = node_ids[node]
        return node    

    def AgirlikliHizliBirlesim_Derinlik(self,node):
        sayac = 0
        while(node != node_ids[node]):
            sayac+=1
            node = node_ids[node]
        return sayac


    def AgirlikliHizliBirlesim_Bul(self, node1,node2):
        return AgirlikliHizliBirlesim_KokBul(node1) == AgirlikliHizliBirlesim_KokBul(node2)
        

    def AgirlikHizliBirlesim_Birlestir(self,node1,node2):
        node1_kok = node_ids[node1]
        node2_kok = node_ids[node2]
        d1 = AgirlikliHizliBirlesim_Derinlik(node1)
        d2 = AgirlikliHizliBirlesim_Derinlik(node2)
        if d1 > d2:
            node_ids[node2] = node1_kok
        else:
            node_ids[node1] = node2_kok

    def PatikaSikistirma_Kokbul(self,node):
        toTheTop = []       
        while(node != node_ids[node]):
            toTheTop.append(node)
            node = node_ids[node]        
        for x in toTheTop:
            self.node_ids[x] = node




    def PatikaSikistirma_Bul(self,node1,node2):
       return PatikaSikistirma_Kokbul(node1) == PatikaSikistirma_Kokbul(node2)


    def PatikaSikistirma_Birlestir(self,node1,node2):
        node1_kok = node_ids[node1]
        node2_kok = node_ids[node2]
        d1 = PatikaSikistirma_Derinlik(node1)
        d2 = PatikaSikistirma_Derinlik(node2)
        if d1 > d2:
            node_ids[node2] = node1_kok
        else:
            node_ids[node1] = node2_kok

    def PatikaSikistirma_Derinlik(self,node):
        sayac = 0
        while(node != node_ids[node]):
            sayac+=1
            node = node_ids[node]
        return sayac
    


