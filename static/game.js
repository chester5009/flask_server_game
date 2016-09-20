/**
 * Created by chester on 17.09.16.
 */


function Player(id,hp,x,y,w,h){
    this.id=id;
    this.hp=hp;
    this.x=x;
    this.y=y;
    this.w=w;
    this.h=h;

}

function Game(context,w,h){
    this.gameState=0; //0-ждёт 1-ищет 2-в игре
    this.myname='unnamed';
    this.ctx=context;
    this.number=0;
    this.uWait=0;
    this.id=null;
    this.players=[];

    this.init=function () {
        player1=new Player(0,0,10,10,30,30);
        player2=new Player(0,0,50,50,30,30);
        this.players.push(player1);
        this.players.push(player2);
    };

    this.render=function () {
        ctx.clearRect(0,0,w,h);
        ctx.fillStyle='#25225D';
        ctx.fillRect(0,0,w,h);
        if(this.gameState==0){
            ctx.font="20px Georgia";
            ctx.fillStyle='#EEEE40';
            ctx.fillText("Ваш id: "+this.myname,10,30);
            ctx.fillText("Пользователей онлайн: "+this.number,10,50);

            ctx.font="32px Impact";
            ctx.fillText("Кликните по экрану для поиска игры",30,250);
        }
        else if(this.gameState==1){
            ctx.font="20px Impact";
            ctx.fillStyle='#EEEE40';
            ctx.fillText("Поиск игры",40,250);

        }
        else if(this.gameState==2){
            ctx.font="20px Impact";
            ctx.fillStyle='#EEEE40';
            ctx.fillText("Нашли соперника",40,250);
            ctx.fillText("ID игры: "+this.id,40,350);

            ctx.fillStyle='#FF0000';
            ctx.fillRect(this.players[0].x,this.players[0].y,this.players[0].w,this.players[0].h);
            ctx.fillStyle='#00FF00';
            ctx.fillRect(this.players[1].x,this.players[1].y,this.players[1].w,this.players[1].h);
           /* сtx.fillStyle='#ff0000';
            ctx.fillRect(this.players[0].x,this.players[0].y,this.players[0].w,this.players[0].h);

            сtx.fillStyle='#00ff00';
            ctx.fillRect(this.players[1].x,this.players[1].y,this.players[1].w,this.players[1].h);*/
        }

    };
    this.update=function (number,uWait,myname) {
        this.myname=myname;
        this.number=number;
        this.uWait=uWait;

    };

    this.setId=function (g) {
        this.id=g;
    };

    this.getId=function () {
        return this.id;
    };

    this.refreshPlayers=function(id1,hp1,x1,y1,id2,hp2,x2,y2){
        this.players[0].x=x1;
        this.players[0].y=y1;
        this.players[0].id=id1;
        this.players[0].hp=hp1;
        this.players[1].x=x2;
        this.players[1].y=y2;
        this.players[1].id=id2;
        this.players[1].hp=hp2;
    }

    this.init();
}
