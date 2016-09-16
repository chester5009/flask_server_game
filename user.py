class User():

    def __init__(self,name,id,lastTime,isEnable):
        self.id=id
        self.name=name
        self.lastTime=lastTime
        self.isEnable=isEnable
        self.status=0 # 0-stay 1-search 2-  in game
    pass


