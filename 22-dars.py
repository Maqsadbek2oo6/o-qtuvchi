oqtuvchi = {'Mamurbek Muxtorov':'123'} 
class Oqtuvchi():
    
    fanlar = {}
    def __init__(self) -> None: 
        pass

    def test(self):
        fan = input("Qaysi fandan test tuzasiz: ").capitalize()
        testlar = input("Testni shu yerga yozing:")
        Oqtuvchi.fanlar[fan] = testlar

    def login(self):
        login1 = input("Ism familiyani kiriting: ").title()
        if login1 in list((oqtuvchi).keys()):
            parol = input("Parolni kiriting: ")
            if parol == oqtuvchi[f"{login1}"]:
                print("Loginga kirdingiz")
                a.test()
            else:
                print("Parol xato")
            
        else:
            print("Login hato")
a = Oqtuvchi()
a.login()