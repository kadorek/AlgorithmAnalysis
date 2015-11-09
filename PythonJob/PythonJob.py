import sys
from Job import Job
import time
import Zaman
from TimeLine import TimeLine
from itertools import *

def main():
    tl= TimeLine(Zaman.Zaman(10,0),Zaman.Zaman(13,0))
    tl.MaksJobLength(30)
    tl.MinJobLength(15)
    
    jobList=[];

    for x in range(10):
        j=Job.CreateJob(tl);
        jobList.append(j)
        j.EkranaJobYaz(tl)
        pass
    jobList.sort(key=lambda x:x.baslangic);

    tumIsUzunluklari= [j.JobLength() for j in jobList ]
    ortalamaIsUzunlugu=sum(tumIsUzunluklari)/(len(tumIsUzunluklari)*1.0)
    baslamaSaatiGruplu=groupby(jobList,lambda x:x.baslangic);
    print "Ortalama is uzunlugu : %f" %ortalamaIsUzunlugu
    print ""
    print ""

    secilenler=[];
    

    for key, group in baslamaSaatiGruplu:
        uyanlar=[j for j in group if j.JobLength()<ortalamaIsUzunlugu ]
        if len(secilenler)==0:
            if len(uyanlar)>0:
                secilenler.append(uyanlar[len(uyanlar)-1])
                pass
            else:
                secilenler.append(group[0]);
                pass
            pass
        else:
            eklendiMi=False
            for j in uyanlar:
                if j.baslangic > secilenler[len(secilenler)-1].bitis:
                    secilenler.append(j);
                    eklendiMi=True
                    break;
                    pass
                pass
            if eklendiMi==False:
                buyukler=[b for b in group if b.JobLength() > ortalamaIsUzunlugu]
                for x in buyukler:
                    if len(secilenler)==0:
                        secilenler.append(x);
                        break;
                        pass
                    if x.baslangic > secilenler[len(secilenler)-1].bitis:
                        secilenler.append(x)
                        pass
                    pass



                pass
            pass

        pass

    for s in secilenler:
        s.EkranaJobYaz(tl)
        pass




    input()
    pass


if __name__ == "__main__":
    sys.exit(int(main() or 0))