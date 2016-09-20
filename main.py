from flask import Flask,render_template,request,session
from flask_socketio import SocketIO, emit ,send,disconnect
from user import User
from game import Game
from multiprocessing import Process
from game import Game
import ssl
import time
import random
import json
import uuid

users=[]
games=[]


app=Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@socketio.on('connect',namespace='/')
def connected():
    print "CONNECTED %s" % (request.remote_addr)+' Session: '+session['']


@socketio.on('disconnect',namespace='/')
def disconnect():
    print "DISconnected"



@socketio.on('info')
def handle_info(data):
    print 'LINKED! '
    info=json.loads(data)
    newid=uuid.uuid4().hex[:8]
    newuser=User(info['name']+str(newid),newid,1,True)
    users.append(newuser)
    emit('my_id',json.dumps({'id':newid}))
    print len(users)


@socketio.on('get_users')
def  handle_get_users(data):
    emit('users_list',json.dumps({'number':len(getUsersNamesList()),'list':getUsersNamesList()}))
    print 'GETTED '

@socketio.on('i_am_here')
def handle_i_am_here(data):
    obj=json.loads(data)
    uid=obj['id']
    ltime=time.time()

    changeLastTime(uid,ltime)

    user=getUserById(uid)

    if(user.isEnable==False):
        if(user in users):
            users.remove(user)
            emit('go_disconnect',{})

    print 'PINGED '+str(uid)+' '+str(ltime)


@socketio.on('change_state')
def handle_change_state(data):
    obj=json.loads(data);
    uid = obj['id']
    newstatus=int(obj['state'])
    for u in users:
        if u.id==uid:
            u.status=newstatus
    emit('change_state',json.dumps({'state':newstatus}))
    print 'State changed!!!!!'

@socketio.on('get_state')
def handle_change_state(data):
    obj=json.loads(data)
    uid = obj['id']

    for u in users:
        if u.id==uid:
            status=u.status
    emit('get_state',json.dumps({'state':status}))

@socketio.on('get_game')
def handle_get_game(data):
    obj=json.loads(data)
    uid=obj['id']
    game = getGameByUser(uid)

    emit('get_game', json.dumps({'id':game.id,'player1':json.dumps(game.players[0].__dict__),'player2':json.dumps(game.players[1].__dict__)}))



@socketio.on('mydisconnect')
def handle_mydisconnect(data):

    userid=json.loads(data)['id']
    print 'DISCONNECTED ' + userid
    disconnect()
    for i in range(len(users)):
        if(i.id==userid):
            users.pop(i)



@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass

'''Logic functions'''

def getUsersNamesList():
    list=[]
    for u in users:
        list.append(u.name)
    return list

def changeLastTime(id,newTime):
    for i in range(len(users)):
        if(users[i].id==id):
            users[i].lastTime= newTime

def isDisconnect():
    for u in users:
        if(u.lastTime+5.0<time.time()):
            u.isEnable=False
    return 0

def deleteLeftUsers():
    for u in users:
        if(u.isEnable==False):
            users.remove(u)

def getUserById(id):
    for u in users:
        if(u.id==id):
            return u
    return False


'''GAME'''

def getGameByUser(uid):
    for game in games:
        for u in game.players:
             if u.id==uid:
                 return game
    return 'no id'

def createNewGame(id1,id2):
    gameid=uuid.uuid4().hex
    new_game=Game(id1,id2,gameid)
    games.append(new_game)


def searcher():
    while True:
        ids=[]
        indexes=[]
        users_searching=0
        users_stay=0
        users_ingame=0


        for i in range(len(users)):

            if users[i].status==0:
                users_stay+=1
            elif users[i].status==1:
                users_searching+=1
            elif users[i].status == 2:
                users_ingame+=1

            if(len(ids)<3):
                if users[i].status==1:
                    ids.append(users[i].id)
                    indexes.append(i)
        print 'SEARCHING: ' + str(users_searching) + ' StAY: ' + str(users_stay)+' InGAME: '+str(users_ingame)
        print 'ALL: '+str(len(users))
        if len(ids)==2:
            users[indexes[0]].status=2
            users[indexes[1]].status=2
            createNewGame(users[indexes[0]].id,users[indexes[1]].id)
        time.sleep(1)

def deleter():
    while True:
        isDisconnect()
        deleteLeftUsers()
        print 'DELETER WORK'
        time.sleep(8)

def gamesUpdater():
    while True:
        for game in games:
            game.run()
            time.sleep(0.033)

if __name__ == '__main__':
    import thread, time,threading

    context = ('cert.crt', 'key.key')

    thread.start_new_thread(lambda: socketio.run(app,host='192.168.1.3',port='9090'), ())

    sThread=threading.Thread(target=searcher)
    deleteThread = threading.Thread(target=deleter)
    gamesUpdThread=threading.Thread(target=gamesUpdater)
    deleteThread.start()
    sThread.start()
    gamesUpdThread.start()

    deleteThread.join()
    sThread.join()
    gamesUpdThread.join()


