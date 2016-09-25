class Enemy():

    def __init__(self,x,y,w,h,dx,dy):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.dx=dx
        self.dy=dy
        self.hp=10
        self.isEnable=True

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        if self.y>480:self.isEnable=False



    pass
