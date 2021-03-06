﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import timeit
import random
from matplotlib import pyplot as plt

#birleştirme-bul temel sınıfı
class UF(object):

    def __init__(self, type,nx,mx):
        self.n = nx
        self.m = mx
        self.nodes = range(0,self.n)
        self.nodes_ids = self.nodes
        self.type = type

    def setNandM(self,nx,mx):
        self.n = nx
        self.m = mx
        self.nodes = range(0,self.n)
        self.nodes_ids = self.nodes
        pass

    def kokbul(self,node):
        while(node != self.nodes_ids[node]):
            node = self.nodes_ids[node]
        return node

    def derinlik(self,node):
        sayac = 0
        while(node != self.nodes_ids[node]):
            sayac+=1
            node = self.nodes_ids[node]
        return sayac

    pass

class QuickFind(UF):
    def __init__(self,nx,mx):
        self.name = u"Hizli Bul"
        self.type = 1
        self.indicator='r--'
        return super(QuickFind, self).__init__(self.type,nx,mx)


    def find(self,node1,node2):
        return self.nodes_ids[node1] == self.nodes_ids[node2]

    def union(self,node1,node2):
        eskiId = self.nodes_ids[node1]
        for x in self.nodes:
            if self.nodes_ids[x] == eskiId:
                self.nodes_ids[x] = self.nodes_ids[node2]
            pass
        pass

    pass

class QuickUnion(UF):
    def __init__(self,  nx, mx):
        self.name = u"Hızlı Birleştir"
        self.type = 2
        self.indicator='bo'
        return super(QuickUnion, self).__init__(self.type, nx, mx)

    def find(self,node1,node2):
        return self.kokbul(node1) == self.kokbul(node2)

    def union(self,node1,node2):
        kok1 = self.kokbul(node1)
        kok2 = self.kokbul(node2)
        self.nodes_ids[kok2] = kok1
        


    pass

class WeightedQuickUnion(UF):
    def __init__(self,  nx, mx):
        self.name = u"Ağırlıklı Hızlı Birleştir"
        self.type = 3
        self.indicator='g^'
        return super(WeightedQuickUnion, self).__init__(self.type, nx, mx)

    def find(self,node1,node2):
        return self.kokbul(node1) == self.kokbul(node2)
    def union(self, node1,node2):
        kok1 = self.kokbul(node1)
        kok2 = self.kokbul(node2)
        d1 = self.derinlik(node1)
        d2 = self.derinlik(node2)
        if d1 > d2:
            self.nodes_ids[kok2] = kok1
        else:
            self.nodes_ids[kok1] = kok2


    pass

class PathCompression(UF):
    def __init__(self,  nx, mx):
        self.name = u"Patika Sıkıştırma"
        self.type = 4
        self.indicator='os'
        return super(PathCompression, self).__init__(self.type, nx, mx)

    def kokbul(self, node):
        toTheTop = []
        while(node != self.nodes_ids[node]):
            toTheTop.append(node)
            node = self.nodes_ids[node]        
        for x in toTheTop:
            self.nodes_ids[x] = node
        return node

    def find(self,node1,node2):
        return self.kokbul(node1) == self.kokbul(node2)

    def union(self ,node1,node2):
        kok1 = self.kokbul(node1)
        kok2 = self.kokbul(node2)
        if kok1==kok2:
            return
        self.nodes_ids[kok1]=kok2
        pass
    pass





def main():

    zamanlar = {}
    
    hizliBul_zamanlar = []
    hizliBirlesim_zamanlar = []
    hizliBirlesimAgirlikli_zamanlar = []
    patikaSikistirma_zamanlar = []
    #
    alar = [QuickFind(1,1),QuickUnion(1,1),WeightedQuickUnion(1,1),PathCompression(1,1)]
    nler = [1000,3000, 5000]
    mler = [10,70,150,300,500]

    plt.figure(figsize=(10,10))
    lines = []
    for k in alar:
        for a in nler:
            zamanlar = []               
            for mx in mler:
                k.setNandM(a,mx)
                start = timeit.default_timer()
                for x in range(1,mx):                
                    n1 = k.nodes[random.randint(0,a - 1)]
                    n2 = k.nodes[random.randint(0,a - 1)]
                    while k.find(n1,n2):
                        n1 = k.nodes[random.randint(0,a - 1)]
                        n2 = k.nodes[random.randint(0,a - 1)]
                    k.union(n1,n2)            
                zamanlar.append(timeit.default_timer() - start)
            nstr=str(a)        
            line = plt.plot(mler,zamanlar,label= k.name + " - n=" + nstr,lw=2)
            lines.append(line)
            print u"Tamamlanan grafik --> Algoritma : "+k.name+" n : "+nstr
    plt.legend(loc="upper left") 
    plt.figtext(.02, .02,u"Birleştir ve Bul algoritmaları karşılaştırılması")  
    plt.ylabel(u"Zaman(~ms)")
    plt.xlabel(u"Birleştirme İşlem Adedi")
    plt.show()
    plt.axis([1,750,0,5])  

    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))

