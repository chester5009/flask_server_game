from player import Player

class Game():

    def __init__(self,id1,id2,id):
        player1=Player(id1,0)
        player2=Player(id2,1)
        self.players = []
        self.players.append(player1)
        self.players.append(player2)
        self.id = id
        pass

    def run(cls):
        pass

    pass





