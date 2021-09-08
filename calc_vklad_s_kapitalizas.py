class Ui_MainWindow(object):
    def __init__(self, vklad, years, stavka):
        self.vklad = vklad
        self.years = years
        self.stavka = stavka

    def bank(self):
        for i in range(self.years):
            self.vklad = self.vklad + (self.vklad / 100 * self.stavka)
        print (self.vklad)

user_1 = Ui_MainWindow(float(input("Введите сумму вклада: ")), int(input("На сколько лет: ")), float(input("Ставка: ")))
user_1.bank()




