import time
from Zaman import Zaman
from TimeLine import TimeLine
from termcolor  import colored
from math import *
from random import randint

class Job(object):
    """description of class"""



    def __init__(self, s,f):
        self.YaziRenkleri = ["yellow","red","green","cyan","gray","magenta"]
        self.baslangic = s
        self.bitis = f
        self.renk = self.YaziRenkleri[randint(0,len(self.YaziRenkleri) - 1)]
        return super(Job, self).__init__()

    def JobLength(self):
        return  -1*Zaman.ZamanFarki(Zaman(self.baslangic.Saat,self.baslangic.Dakika),Zaman(self.bitis.Saat,self.bitis.Dakika))

    def EkranaJobYaz(self,tl):

        fark = Zaman.ZamanFarki(self.baslangic,tl.DayStart)
        for x in range(0,(fark / 5)):
            print "-", 

        for x in range(0,(self.JobLength() / 3)):
            print "*",
            
        sonFark = Zaman.ZamanFarki(self.bitis,tl.DayFinish)
        for x in range(0,(sonFark / 5)):
            print "-",       

        print "%d:%d(%d dk.)" % (self.baslangic.Saat , self.baslangic.Dakika,self.JobLength()) 
        pass    


   
    @staticmethod
    def CreateJob(tl):
        j = Job(Zaman(-1,-1),Zaman(-1,-1))
        while(j.JobLength() > tl.MaksJL() or j.JobLength() < tl.MinJL()):
            baslangicAt = randint(0,tl.DayLengthMinute() - tl.MaksJL())
            rndBasDak = baslangicAt % 60
            rndBasSaat = baslangicAt / 60
            Saat = tl.DayStart.Saat + rndBasSaat
            Dakika = tl.DayStart.Dakika + rndBasDak
            j.baslangic=Zaman(Saat,Dakika)
            sureAt = randint(tl.MinJL(),tl.MaksJL())
            j.bitis = Zaman.AddMinuteToZaman(Zaman(j.baslangic.Saat,j.baslangic.Dakika),sureAt)
            pass

        return j
        pass

    def __str__(self):
        return  "%d:%d-%d:%d" %(self.baslangic.Saat,self.baslangic.Dakika,self.bitis.Saat,self.bitis.Dakika)