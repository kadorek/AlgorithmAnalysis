from Zaman import Zaman
class TimeLine(object):
    """description of class"""


    def __init__(self, s,f):
        self.DayStart = s
        self.DayFinish = f
        return super(TimeLine, self).__init__()
    
    def MaksJobLength(self,value=0):
        self._MaksJobLength = value
                
    def MinJobLength(self,value=0):
        self._MinJobLength = value

    def MaksJL(self):
        return self._MaksJobLength
    
    def MinJL(self):
        return self._MinJobLength
    
    def DayLengthMinute(self):
        return Zaman.ZamanFarki(self.DayFinish,self.DayStart);