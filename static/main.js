/**
 * Created by chester on 12.09.16.
 */
var socket=io('http://'+document.domain+':'+location.port);
var my_id;
var lastTime=0;

var timerPinger=0;
var timerGetUsers=0;
socket.on('connect',function () {

});
window.onunload = function()
{
    socket.disconnect();

    //socket.emit('mydisconnect',JSON.stringify({id:my_id}));
    return confirm('Вы хотите покинуть сайт?')
}
window.onbeforeunload = function(){
    socket.disconnect();

    //socket.emit('mydisconnect',JSON.stringify({id:my_id}));
    return confirm('Точно хотите выйти?');
}

$(document).ready(function () {
    $('#content').hide();
    socket.on('users_list',function (data) {

        var list=JSON.parse(data);
        console.log(list);
        var names=list['list'];
        var content='';
        $("#answer").html('');
        content+='Пользователей в сети '+list['number'];
        content+='<br>';
        $("#answer").append('Пользователей в сети '+list['number']);
        for (var i=0;i<names.length;i++){
            //$("#answer").append('< br>');
            //$("#answer").append(names[i]);
            content+='<br>';
            content+=names[i]+' ';

        }
        $('#answer').html(content);
    });

    socket.on('my_id',function (data) {
        var json=JSON.parse(data);
        my_id=json['id'];
        $('#head').append(' id: '+my_id);
    });

    socket.on('go_disconnect',function (data) {
        socket.disconnect();
    });

    $('#ok').click(function () {
        var nick=$('#nick').val();
        sendInfo(socket,nick);
        $('#content').show();
        $('#enter').hide();
    });

    update();
});




function sendInfo(socket,nick) {
    socket.emit('info',JSON.stringify({name:nick}));

}
function getUsers(socket){
    socket.emit('get_users','');

}
function imHere(socket) {
    lastTime=Date.now();
    socket.emit('i_am_here',JSON.stringify({id:my_id,time:lastTime}));
}


function update() {
    timerPinger+=1;
    timerGetUsers+=1;
    if(timerGetUsers>50){
        console.log('getUSERs');
        getUsers(socket);
        timerGetUsers=0;
    }
    if(timerPinger>10){
        console.log('ping!');
        imHere(socket);
        timerPinger=0;
    }

    requestAnimationFrame(update);
}

/*setInterval(function () {
 timerPinger+=1;
 timerGetUsers+=1;
 if(timerGetUsers>400){
 console.log('getUSERs');
 getUsers(socket);
 timerGetUsers=0;
 }
 if(timerPinger>200){
 console.log('ping!');
 imHere(socket);
 timerPinger=0;
 }
 },10);*/