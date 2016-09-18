/**
 * Created by chester on 17.09.16.
 */
function Game(context,w,h){
    this.gameState=0; //0-ждёт 1-ищет 2-в игре
    this.myname='unnamed';
    this.ctx=context;
    this.number=0;
    this.uWait=0;


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
        }

    };
    this.update=function (number,uWait,myname) {
        this.myname=myname;
        this.number=number;
        this.uWait=uWait;
    };
}