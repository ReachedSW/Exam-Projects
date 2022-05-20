import random as rnd
from tabnanny import check

from barbut import controlChecks


class Barbut():
    def __init__(self):
        self.winningNums = [7,11]
        self.barbutNums = [2,3,12]
        self.reCheckNums = [4,5,6,8,9,10]
        self.check1 = 0
        self.check2 = 0
    def zarAt(self):
        self.check1, self.check2 = rnd.randint(1,6), rnd.randint(1,6)
        print("Atılan zarlar : {x} + {y} = {sum}".format(x =self.check1, y = self.check2, sum = self.check1+self.check2))
        return self.check1 + self.check2
    
    def controlChecks(self, checkSum):
        if checkSum in self.winningNums:
            print("Tebrikler, kazandınız !")
            return False
        elif checkSum in self.barbutNums:
            print("Barbut! Kaybettiniz.")
            return False
        else:
            return True
    
    def gameProcces(self):
        print("<System> Zar atılıyor...")
        checkSum = self.zarAt()
        print("Atılan zarların toplamı = {x}".format(x = checkSum))

        if controlChecks(checkSum=checkSum) == False:
            print("Oyun bitti")
        elif checkSum in self.reCheckNums:
            print("\nSon şanslar! Tekrar aynı zarı atarsanız kazanırsınız.\n-> Dikkat! Eğer 7 atarsan kaybedersin.\n")
            bReak = True
            while bReak:
                newCheck = self.zarAt()
                if newCheck == 7:
                    print("Kaybettiniz.")
                    bReak = False
                elif newCheck == checkSum:
                    print("Kazandınız !")
                    bReak = False


barbutGame = Barbut()

barbutGame.gameProcces()