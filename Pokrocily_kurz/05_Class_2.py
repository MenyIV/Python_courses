class Robot:
    
    
    #konstructor
    def __init__(self, baterie,delka_rukou):
        self.bat=baterie
        self.ruk=delka_rukou
        self.cykl=1000

    def cyklus(self):
        print("pocitadlo cyklu")
        self.cykl -=1
    
    def krok_vpred(self):
        print("Robot jde vpred")
        self.cykl -=1
        
    def krok_vzad(self):
        print("Robot jde vzad")
        self.cykl -=1




#vytvořemní objektu podle klaaasy
robot_1 = Robot(24,0.6)
robot_2 = Robot(48,1)
robot_3 = Robot(15,0.4)
robot_4 = Robot(10,2)




robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()

robot_1.krok_vzad()
robot_1.krok_vzad()
robot_1.krok_vzad()
robot_1.krok_vzad()


print (robot_1.cykl)
print (robot_2.ruk)