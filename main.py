from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit ,send
from usersinfo import Users
from user import User
import json
u=Users()
users=[]



app=Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app)



@app.route('/')
def index():
    return render_template('auth.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@socketio.on('connect',namespace='/')
def connected():

    print "CONNECTED "

@socketio.on('disconnect',namespace='/')
def disconnect():
    print "DISconnected"



@socketio.on('info')
def handle_info(data):
    print 'LINKED! '
    info=json.loads(data)
    newuser=User(info['name'])
    users.append(newuser)
    print len(users)


@socketio.on('get_users')
def  handle_get_users(data):
    emit('users_list',json.dumps({'number':len(getUsersNamesList()),'list':getUsersNamesList()}))
    print 'GETTED '

def send_user_info():

    pass

@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass


def getUsersNamesList():
    list=[]
    for u in users:
        list.append(u.name)
    return list
if __name__ == '__main__':
    socketio.run(app,host='192.168.1.3',port='9090')
