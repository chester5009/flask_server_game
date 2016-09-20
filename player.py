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

    def setCoordinates(self):
        if self.place==0:
            self.x=30
            self.y=400
        elif self.place==1:
            self.x=500
            self.y=400

    def update(self):
        self.move(2)
        pass

    def move(self,dir): #0-left 1-left 2-right
        if dir==1:
            self.x-=2
        elif dir==2:
            self.x+=2

    pass
