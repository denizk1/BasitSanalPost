# Sanal post entegresyonumuzdaki data
data = {
    0: {"name": "ali", "surname": "dogan", "cardnumber": "1234123256781234", "cvv": "123", "limit": "500",
        "validdate": "8/20"},
    1: {"name": "ragip", "surname": "basbug", "cardnumber": "1234123256781235", "cvv": "123", "limit": "500",
        "validdate": "8/20"}}


class Card(object):
    # Kart bilgileri
    def __init__(self, name, surname, cardnumber, cvv, amountPay, validdate):
        self.id = -1
        self.name = name
        self.surname = surname
        self.cardnumber = cardnumber
        self.cvv = cvv
        self.amountPay = amountPay
        self.validdate = validdate

        # Kart bilgilerinin mevcut olup olmadiginin kontrolu
        self.namebool = False
        self.surnamebool = False
        self.cardnumberbool = False
        self.cvvbool = False
        self.amountPaybool = False
        self.validdatebool = False

    def is_name(self, datanumber):
        if (self.name == datanumber["name"]):
            self.namebool = True

    def is_surname(self, datanumber):
        if (self.surname == datanumber["surname"]):
            self.surnamebool = True

    def is_cardnumber(self, datanumber):
        if (self.cardnumber == datanumber["cardnumber"]):
            self.cardnumberbool = True

    def is_cvv(self, datanumber):
        if (self.cvv == datanumber["cvv"]):
            self.cvvbool = True

    def is_amountPay(self, datanumber):
        if (int(self.amountPay) <= int(datanumber["limit"])):
            self.amountPaybool = True

    def is_validdate(self, datanumber):
        if (self.validdate == datanumber["validdate"]):
            self.validdatebool = True

    def is_data(self, data):
        for i, j in enumerate(data):
            self.id = i
            self.is_name(data[i])
            self.is_surname(data[i])
            self.is_cardnumber(data[i])
            self.is_cvv(data[i])
            self.is_amountPay(data[i])
            self.is_validdate(data[i])

            # Eger datanin icinde  bilgileri bulursa dongu dursun
            if (self.namebool == True) and (self.surnamebool == True) and (self.cardnumberbool == True) and (
                    self.cvvbool == True) and (self.validdatebool == True) and (self.amountPaybool == True):
                data[self.id]["limit"] = str(int(data[self.id]["limit"]) - int(self.amountPay))
                self.id = i
                break
            else:
                continue

        # Bilgiler mevcutsa islem gerceklessin
        if (self.namebool == True) and (self.surnamebool == True) and (self.cardnumberbool == True) and (
                self.cvvbool == True) and (self.validdatebool == True) and (self.amountPaybool == True):
            print("isleminiz basariyla gerceklestirilmistir...")

            # islem gerceklesirse kartin kullanilabilir limitini güncelle
            data[self.id]["limit"] = str(int(data[self.id]["limit"]) - int(self.amountPay))

        # Eger bilgiler mevcut degilse kart gecerli degildir
        elif (self.namebool != True) or (self.surnamebool != True) or (self.cardnumberbool != True) or (
                self.cvvbool != True) or (self.validdatebool != True):
            print("boyle bir kart mevcut degildir...Lütfen tekrar deneyin")

        # Eger bilgiler mevcutsa fakat limit yetersiz ise islem gecersiz olsun
        elif (self.namebool == True) and (self.surnamebool == True) and (self.cardnumberbool == True) and (
                self.cvvbool == True) and (self.validdatebool == True) and (self.amountPaybool != True):
            print("limitiniz yetersiz...Lütfen tekrar deneyin")


card = Card("ali", "dogan", "1234123256781234", "123", "400", "8/20")
card.is_data(data)

card = Card("zeynep", "dogan", "1234123256781234", "123", "400", "8/20")
card.is_data(data)

card = Card("ragip", "basbug", "1234123256781235", "123", "1000", "8/20")
card.is_data(data)