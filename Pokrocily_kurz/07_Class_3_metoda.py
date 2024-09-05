class Robot:
    
    
    #konstructor
    def __init__(self, baterie,delka_rukou):
        self.bat=baterie
        self.ruk=delka_rukou
        self.cykl=1000


#vytvořemní objektu podle klaaasy
robot_1 = Robot(24,0.6)
robot_2 = Robot(48,1)
robot_3 = Robot(15,0.4)
robot_4 = Robot(10,2)

print(robot_1.bat)
print(robot_1.ruk)
print(robot_1.cykl)

print(robot_2.bat)
print(robot_2.ruk)
print(robot_2.cykl)

print(robot_3.bat)
print(robot_3.ruk)
print(robot_3.cykl)

print(robot_4.bat)
print(robot_4.ruk)
print(robot_4.cykl)
