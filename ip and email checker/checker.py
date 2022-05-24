aNumericThings = []

sLetters = "abcçdefgğhıijklmnoöprsştuüvyzqw"
scapitalLetters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQW"
sNumeric = "1234567890"

# print(numericThings)

class Checker():
    def __init__(self, mail = "", ip_address = ""):
        self.mail = mail
        self.ip_adress = ip_address
        self.mail_status = True
        self.ip_status = True

    def checkMail(self):
        #check tag count
        tagCount = 0
        for i in self.mail:
            if i == "@":
                tagCount += 1
        
        if tagCount > 1:
            print("@ İşareti maksimum bir adet olabilir.")
            self.mail_status = False
            return False
        #end check tag count

        #split mail before and after "@"
        tempMail = self.mail.split('@')
        beforeTag = tempMail[0]
        afterTag = tempMail[1]
        #end splitting

        #CHECK BEFORE
        
        #CHECK LENGTH OF BEFORETAG
        if len(beforeTag) <1:
            print("E-mail adresi en az 1 karakter içermelidir.")
            self.mail_status = False
            return False
        #END CHECK LENGTH OF BEFORETAG
        
        #CHECK LETTER MUST BE IN OF BEFORETAG
        bLetterCheck = True

        for i in beforeTag:
            if i not in sLetters or i not in scapitalLetters:
                bLetterCheck = False
            else:
                bLetterCheck = True
                break

        # for i in sLetters:
        #     if i in beforeTag:
        #         continue
        #     else:
        #         bLetterCheck = False
        #         break

        if not bLetterCheck:
            print("En az bir adet sözel karakter içermelidir.")
            self.mail_status = False
            return False
        #ENDCHECK LETTER MUST BE IN OF BEFORETAG
        
        #END CHECK BEFORE

        
        #CHECK AFTER TAG
        
        # CHECK LENGTH OF AFTER TAG

        if len(afterTag) < 5:
            print("@ İşaretinin sağ tarafında en az 4 karakter olmalı")
            self.mail_status = False
            return False

        # END CHECK LENGTH OF AFTER TAG

        # DOT CHECK AFTER TAG

        if "." not in afterTag:
            print("@ İşaretinin sağ tarafında bir adet nokta bulunmalıdır.")
            self.mail_status = False
            return False
        
        iDotCount = 0

        for i in afterTag:
            if i == ".":
                iDotCount += 1
        
        if iDotCount > 1:
            print("@ İşaretinin sağ tarafında en çok bir tane nokta işareti bulunabilir.")
            self.mail_status = False
            return False
        

        # END DOT CHECK AFTER TAG


        #END AFTER TAG
          

    def getMailStatus(self):
        return self.mail_status


    def checkIp(self):
        bStatus = True

        ipAdress = self.ip_adress.split(".")
        
        if len(ipAdress) > 4:
            # print("Geçersiz ip adresi")
            self.ip_status = False
            return False
        
        

        # firstDot = int(ipAdress[0])
        # secDot = int(ipAdress[1])
        # thirdDot = int(ipAdress[2])
        # fourthDot = int(ipAdress[3])

        for i in ipAdress:
            if int(i) < 0 or int(i) > 255:
                # print("Geçersiz ip adresi")
                bStatus = False
                self.ip_status = False
                break
                

        if not bStatus:
            return False


    def getIpStatus(self):
        return self.ip_status
