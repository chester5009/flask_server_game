from flask import Flask,render_template,request,session
from flask_socketio import SocketIO, emit ,send,disconnect
from usersinfo import Users
from user import User
import time
import random
import json
u=Users()
users=[]



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
    newid=random.randint(1,99999999)
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

@socketio.on('mydisconnect')
def handle_mydisconnect(data):

    userid=json.loads(data)['id']
    print 'DISCONNECTED ' + userid
    disconnect()
    for i in range(len(users)):
        if(i.id==userid):
            users.pop(i)

def send_user_info():

    pass

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

if __name__ == '__main__':
    import thread, time
    thread.start_new_thread(lambda: socketio.run(app,host='192.168.1.3',port='9090'), ())
    while True:
        time.sleep(15)
        isDisconnect()
        deleteLeftUsers()
