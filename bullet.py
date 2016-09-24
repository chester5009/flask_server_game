class Bullet():

    def __init__(self,x,y,w,h,dx,dy):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.dx=dx
        self.dy=dy
        self.isEnable=True

    def update(self):
        self.y+=self.dy
        self.x+=self.dx
        if self.y+self.h<0:
            self.isEnable=False

    pass


