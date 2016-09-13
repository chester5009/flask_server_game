/**
 * Created by chester on 12.09.16.
 */
console.log('ahahah')
var socket=io.connect('http://'+document.domain+':'+location.port);
socket.on('connect',function () {
    socket.emit('my_event',{data:'I am connected!'});
});