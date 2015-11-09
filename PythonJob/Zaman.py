class Zaman(object):
    """description of class"""

    def __init__(self, h,m):
        self.Saat = h
        self.Dakika = m
        if m > 59:
            self.Saat+=(m - (m % 60)) / 60
            self.Dakika = m % 60
            pass
        return super(Zaman, self).__init__()

    def ZamanFarki(z1,z2):
        """İki zaman arasındaki dakika farkı"""

        if z1.Saat < z2.Saat:
            g = z1
            z1 = z2
            z2 = g
        
        if z1.Dakika < z2.Dakika:
            z1.Saat-=1
            z1.Dakika+=60

        sonuc = (z1.Saat - z2.Saat) * 60 + z1.Dakika - z2.Dakika
        return sonuc


    def AddMinute(self,minute):
        d = minute % 60
        s = (minute - d) / 60
        self.Saat+=s
        self.Dakika+=d

        if self.Dakika > 59:
            self.Saat+=1
            self.Dakika-=60
            pass

    def AddMinuteToZaman(z,minute):
        z.AddMinute(minute)
        return z
        pass

    def __gt__(self,z):
        m1 = self.Saat * 60 + self.Dakika
        m2 = z.Saat * 60 + z.Dakika
        return m1 > m2

