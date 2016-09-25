from player import Player
from enemy import Enemy
import time
import random

class Game():

    def __init__(self,id1,id2,id):
        player1=Player(id1,0)
        player2=Player(id2,1)
        self.players = []
        self.enemys=[]
        self.players.append(player1)
        self.players.append(player2)
        self.id = id
        self.timer=time.time()
        self.spawnTimer=0
        pass

    def run(self):
        delta=time.time()-self.timer
        self.timer=time.time()
        self.spawnTimer+=delta
        if self.spawnTimer>1.5:
            self.enemySpawn()
            self.spawnTimer=0
        for p in self.players:
            p.update()
        for e in self.enemys:
            e.update()
        self.intersectionEnemys()

        pass

    def intersectionEnemys(self):
        for i in range(len(self.enemys)):
            for j in range(len(self.players)):
                for m in range(len(self.players[j].bullets)):
                    e=self.enemys[i]
                    b=self.players[j].bullets[m]
                    if self.intersectionFunction(e.x,e.y,e.w,e.h,b.x,b.y,b.w,b.h)==False:
                        self.players[j].bullets.remove(b)
                        self.enemys.remove(e)
                        --i
                        --m
                        return

        '''for e in reversed(self.enemys):
            for p in reversed(self.players):
                for b in reversed(p.bullets):
                    if self.intersectionFunction(e.x,e.y,e.w,e.h,b.x,b.y,b.w,b.h)==True:
                        p.bullets.remove(b)
                        self.enemys.remove(e)'''


    def intersectionFunction(self,X1,Y1,W1,H1,X2,Y2,W2,H2):
        if (X1 + W1 < X2 or X2 + W2 < X1 or Y1 + H1 < Y2 or Y2 + H2 < Y1):
            return True
        else:
            return False


    def enemySpawn(self):
        newEnemy=Enemy(random.randint(0,610),-30,30,30,0,4)
        self.enemys.append(newEnemy)
    pass





