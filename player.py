from bullet import Bullet

class Player():

    def __init__(self,id,place):
        self.id=id
        self.hp=100
        self.x=0;
        self.y=0
        self.w=20
        self.h=20
        self.place=place
        self.setCoordinates()
        self.keys=[0]*1100
        self.bullets=[]

    def setCoordinates(self):
        if self.place==0:
            self.x=30
            self.y=400
        elif self.place==1:
            self.x=500
            self.y=400

    def update(self):
        self.move()
        if self.keys[32]==1:
            self.shotting()
        for bullet in self.bullets:
            bullet.update()
            if bullet.isEnable==False:
                self.bullets.remove(bullet)
        pass

    def move(self):
        if (self.keys[65]==1):
            self.x-=4
        if (self.keys[68] == 1):
            self.x+=4

    def shotting(self):
        newBullet=Bullet(self.x,self.y,5,5,0,-14)
        self.bullets.append(newBullet)

    pass
