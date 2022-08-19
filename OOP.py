print("Служащий,персона,рабочий,инженер")

class Angestellter():
    def __init__(self, Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt):
        self.Index = Index
        self.Arbeit_status = Arbeit_status
        self.Arbeitserfahrung = Arbeitserfahrung
        self.Gehalt = Gehalt
        self.Jahre_alt = Jahre_alt

class Person(Angestellter):
    def __init__(self, Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt):
        super().__init__(Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt)
    @staticmethod
    def Pension(Jahre_alt, Arbeitserfahrung):
        if(Jahre_alt>64):
            return (Jahre_alt+Arbeitserfahrung)
        if(Jahre_alt<=64):
            return 0
    def Steuer(Jahre_alt,Arbeitserfahrung):
        if(Pension):
            return (Jahre_alt+Arbeitserfahrung)/2
        else:
            return (Gehalt-5)/2


class Arbeiter(Angestellter):
    def __init__(self, Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt):
        super().__init__(Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt)
    @staticmethod
    def Arbeit(Arbeit_status):
        if(Arbeit_status=="Ya"):
            return True
        else:
            return False
            
class Ingenieur(Angestellter):
    def __init__(self, Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt):
        super().__init__(Index, Arbeit_status, Arbeitserfahrung, Gehalt, Jahre_alt)
    @staticmethod
    def Zp(Gehalt,Arbeit_status,Jahre_alt):
        if(Arbeit_status=="Ja" and Jahre_alt>20):
            return Gehalt*2
        else:
            return Gehalt


Jahre_alt=int(input("Ваш возраст "))
Index=str(input("Ваш индекс "))
Arbeit_status=str(input("Ваш рабочий статус "))
Arbeitserfahrung=int(input("Ваш опыт в работе "))
Gehalt=int(input("Ваша заработная плата "))

a=Person(Index,Arbeit_status,Arbeitserfahrung,Gehalt,Jahre_alt)
b=Arbeiter(Index,Arbeit_status,Arbeitserfahrung,Gehalt,Jahre_alt)
c=Ingenieur(Index,Arbeit_status,Arbeitserfahrung,Gehalt,Jahre_alt)

Signal = True

print("Пользователь", Index,"Все данные класса представлены:")
print("Пенсия:",a.Pension(Jahre_alt, Arbeitserfahrung))
aaa=b.Arbeit(Arbeit_status)
if(aaa!=Gehalt):
    print("Вы не безработны")
else:
    print("Найдите работу")
bbb=c.Zp(Gehalt,Arbeit_status,Jahre_alt)
if(bbb):
    print("Вам присваивается дополнительные выплаты за продожительность работы: ",bbb)
else:
    print("К сожалению,ничего :(")
