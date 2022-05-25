import checker

def check():
    inptCounter = 0 

    while inptCounter < 5:
    
        userSelect = int(input("Lütfen yapmak istediğiniz işlemi seçiniz;\n1->E-mail\n2->IP Adress\nSeçiminiz : "))

        if userSelect == 1:
            userEmail = input("Lütfen e-mail'inizi giriniz : ")
            checker = checker.Checker(mail = userEmail)
            checker.checkMail()
            if checker.getMailStatus():
                print("Geçerli e-mail adresi.")
            else:
                print("Geçersiz e-mail adresi.")

        else:
            userIp = input("Lütfen IP Adresinizi giriniz: ")
            checker = checker.Checker(ip_address=userIp)
            checker.checkIp()
            if checker.getIpStatus():
                print("Geçerli ip adresi")
            else:
                print("Geçersiz ip adresi")

        inptCounter += 1



if __name__ == "__main__":
    check()