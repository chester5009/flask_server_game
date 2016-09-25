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
    this.bullets=[];
}

function Game(context,w,h){
    this.gameState=0; //0-ждёт 1-ищет 2-в игре
    this.myname='unnamed';
    this.ctx=context;
    this.number=0;
    this.uWait=0;
    this.id=null;
    this.players=[];
    this.enemys=[];

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
            ctx.fillStyle='#FF0000';
            ctx.fillRect(this.players[0].x,this.players[0].y,this.players[0].w,this.players[0].h);
            ctx.fillStyle='#00FF00';
            ctx.fillRect(this.players[1].x,this.players[1].y,this.players[1].w,this.players[1].h);
           /* сtx.fillStyle='#ff0000';
            ctx.fillRect(this.players[0].x,this.players[0].y,this.players[0].w,this.players[0].h);

            сtx.fillStyle='#00ff00';
            ctx.fillRect(this.players[1].x,this.players[1].y,this.players[1].w,this.players[1].h);*/
            for (var i=0;i<this.players[0].bullets.length;i++){
                var bullet=this.players[0].bullets[i];
                ctx.fillStyle='#FF0000';
                ctx.fillRect(bullet.x,bullet.y,bullet.w,bullet.h);
            }

            for (var i=0;i<this.players[1].bullets.length;i++){
                var bullet=this.players[1].bullets[i];
                ctx.fillStyle='#00FF00';
                ctx.fillRect(bullet.x,bullet.y,bullet.w,bullet.h);
            }

            for (var i=0;i<this.enemys.length;i++){
                var enemy=this.enemys[i];
                ctx.fillStyle='#A4A9F6';
                ctx.fillRect(enemy.x,enemy.y,enemy.w,enemy.h);
            }

            ctx.font="20px Impact";
            ctx.fillStyle='#EEEE40';
            ctx.fillText("Нашли соперника",40,50);
            ctx.fillText("ID игры: "+this.id,40,100);
            ctx.fillText("Демо игры",40,150);
            ctx.fillText("A <- D -> Space shot",40,200);
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

    this.refreshPlayers=function(id1,hp1,x1,y1,bullets1,id2,hp2,x2,y2,bullets2){
        this.players[0].x=x1;
        this.players[0].y=y1;
        this.players[0].id=id1;
        this.players[0].hp=hp1;
        this.players[0].bullets=bullets1;

        this.players[1].x=x2;
        this.players[1].y=y2;
        this.players[1].id=id2;
        this.players[1].hp=hp2;
        this.players[1].bullets=bullets2;
    };
    
    this.refreshEmemys=function (enemys) {
        this.enemys=enemys;
    };

    this.init();
}
