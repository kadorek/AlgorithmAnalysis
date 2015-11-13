﻿import sys
import math
import timeit
import random



def main():

   


    pass



if __name__ == "__main__":
    sys.exit(int(main() or 0))


class Question:

    def __init__(self):
        self.n = random.randint(20,1000)
        self.m = random.randint(10,n / 2)
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
        pass
    
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

      

    


