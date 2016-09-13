from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit ,send
from usersinfo import Users
from user import User
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
    newuser=User(request.namespace.socket.sessid,'f')
    users.append(newuser)
    u.n = len(users)
    print "CONNECTED "+newuser.id

'''
@socketio.on('disconnect',namespace='/')
def disconnected():
    u.decr()
    print "DISCONNECTED "
'''


@socketio.on('my event')
def handle_my_event(data):
    print 'DATA:'

    emit('answer',u.n)
    return 1


@socketio.on('get_user_number')
def  handle_get_user_number(data):
    emit('user_nubmers',u.n)


def send_user_info():

    pass

@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass




if __name__ == '__main__':
    socketio.run(app,host='192.168.1.3',port='9090')
