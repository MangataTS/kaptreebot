import os
from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event, Message
from aiocqhttp import MessageSegment

#语音包指令

#早上好啊，小哥哥
cmd1 = on_command('早上好',aliases={'早安'},priority=2)
@cmd1.handle()
async def cmd1_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\zsh.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我傻呗
cmd2 = on_command('你为什么喜欢上我',priority=2)
@cmd2.handle()
async def cmd2_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我傻呗.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#晚安咯，我要去睡觉了，不然该不漂亮了
cmd3 = on_command('晚安',priority=2)
@cmd3.handle()
async def cmd3_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\晚安咯，我要去睡觉了，不然该不漂亮了.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#
cmd4 = on_command('今晚到我房间来',priority=2)
@cmd4.handle()
async def cmd4_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我已经躺床上了.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#能做你女朋友吗
cmd5 = on_keyword(['单身'],priority=2)
@cmd5.handle()
async def cmd5_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我能做你女朋友吗？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#哎呀好的啦 小哥哥不要生气了嘛
cmd6 = on_keyword(['生气','气死我','是遇得到','服了','醉了','不高兴','不开心','好烦'],priority=2)
@cmd6.handle()
async def cmd6_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\。哎呀好的啦 小哥哥不要生气了嘛.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你好小哥哥，需要服务吗？
cmd7 = on_command('hello',priority=2)
@cmd7.handle()
async def cmd7_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你好小哥哥，需要服务吗？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不要想那么多。想太多不好
cmd8 = on_command('我总是想太多',priority=2)
@cmd8.handle()
async def cmd8_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不要想那么多。想太多不好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#忙什么，都不知道找我聊聊天
cmd9 = on_keyword(['好忙','事情好多','事好多'],priority=2)
@cmd9.handle()
async def cmd9_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\忙什么，都不知道找我聊聊天.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#才不话音视频呢，太轻浮了。
cmd10 = on_command('来视频吧',priority=2)
@cmd10.handle()
async def cmd10_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\才不话音视频呢，太轻浮了。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我会努力的
cmd11 = on_command('你整天就玩吗',priority=2)
@cmd11.handle()
async def cmd11_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我会努力的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我的红包呢
cmd12 = on_keyword(['红包'],priority=2)
@cmd12.handle()
async def cmd12_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我的红包呢.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#我这不方便接语音，打字聊行么？
cmd13 = on_command('语音吗',priority=2)
@cmd13.handle()
async def cmd13_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我这不方便接语音，打字聊行么？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#拜拜咯，我去洗澡了。.mp3
cmd14 = on_command('待会聊',priority=2)
@cmd14.handle()
async def cmd14_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\拜拜咯，我去洗澡了。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#叫我小仙女
cmd15 = on_command('怎么称呼你呢',aliases={'叫你什么呢','你叫什么呢','你叫啥','你的名字是什么'},priority=2)
@cmd15.handle()
async def cmd15_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\叫我小仙女.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你好帅啊
cmd16 = on_command('我帅吗',aliases={'我长得怎么样','我好看吗'},priority=2)
@cmd16.handle()
async def cmd16_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你好帅啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我单身啊
cmd17 = on_command('你有男朋友吗',aliases={'单身吗'},priority=2)
@cmd17.handle()
async def cmd17_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我单身啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你为什么会问这个问题~1.mp3
cmd18 = on_command('我和你妈掉进水里',priority=2)
@cmd18.handle()
async def cmd18_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你为什么会问这个问题~1.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我tm说我不是女的，你tm是要搞基。.mp3
cmd19 = on_command('小姐姐处CP吗',aliases={'谈恋爱吗','网恋吗','处CP吗'},priority=2)
@cmd19.handle()
async def cmd19_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我tm说我不是女的，你tm是要搞基。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我的错咯。要不要道个歉？
cmd20 = on_command('都怪你',aliases={'都是你的错'},priority=2)
@cmd20.handle()
async def cmd20_(bot:Bot,event:Event):
    if int(event.get_user_id())!= event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我的错咯。要不要道个歉？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我平常不喜欢语音的，很少说话.mp3
cmd21 = on_command('你很喜欢发语音吗',aliases={'你怎么总是发语音','你怎么老是发语音'},priority=2)
@cmd21.handle()
async def cmd21_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我平常不喜欢语音的，很少说话.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我身体不舒服就别强迫我啦。.mp3
cmd22 = on_command('今晚来玩吗',aliases={'出来玩'},priority=2)
@cmd22.handle()
async def cmd22_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我身体不舒服就别强迫我啦。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我身体不舒服就别强迫我啦。.mp3
cmd23 = on_command('抱抱',priority=2)
@cmd23.handle()
async def cmd23_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我要抱抱.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd24 = on_command('你在想什么',priority=2)
@cmd24.handle()
async def cmd24_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我再想你啊小笨蛋.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我最喜欢喝牛奶了 旺仔牛奶耶耶耶
cmd25 = on_command('你喜欢喝什么',aliases={'你最喜欢喝什么'},priority=2)
@cmd25.handle()
async def cmd25_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我最喜欢喝牛奶了 旺仔牛奶耶耶耶.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#油嘴滑舌的
cmd26 = on_command('你真好看',aliases={'你好漂亮','你真美'},priority=2)
@cmd26.handle()
async def cmd26_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\油嘴滑舌的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#就算搞基我也只做攻 就是把你压在身下那种。
cmd27 = on_command('击剑吗',aliases={'击剑嘛','来击剑'},priority=2)
@cmd27.handle()
async def cmd27_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\就算搞基我也只做攻 就是把你压在身下那种。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不要因为我可爱你就欺负我.mp3
cmd28 = on_command('你好可爱',aliases={'你真可爱'},priority=2)
@cmd28.handle()
async def cmd28_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不要因为我可爱你就欺负我.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#对对对，这是下载的.mp3
cmd29 = on_command('你这是下载的吗',aliases={'你的语音是下载'},priority=2)
@cmd29.handle()
async def cmd29_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\对对对，这是下载的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#嗯嗯，你对我真好.mp3
cmd30 = on_command('我对你好吗',aliases={'我对你好不好'},priority=2)
@cmd30.handle()
async def cmd30_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\嗯嗯，你对我真好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#哇你好棒棒哦.mp3
cmd31 = on_command('我棒不棒',aliases={'厉害吧'},priority=2)
@cmd31.handle()
async def cmd31_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\哇你好棒棒哦.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我不信.mp3
cmd32 = on_command('我不喜欢你了',aliases={'你不好看'},priority=2)
@cmd32.handle()
async def cmd32_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我不信.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#其实我也腼腆.mp3
cmd33 = on_command('我有点害羞',aliases={'我有点内向','我很内向'},priority=2)
@cmd33.handle()
async def cmd33_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\其实我也腼腆.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你再这样我不理你了啊.mp3
cmd34 = on_command('跳个舞',aliases={'来跳个舞'},priority=2)
@cmd34.handle()
async def cmd34_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你再这样我不理你了啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你以后要只对我一个人好.mp3
cmd35 = on_command('我喜欢你',aliases={'我稀饭你'},priority=2)
@cmd35.handle()
async def cmd35_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你以后要只对我一个人好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#别老色迷迷的好不好.mp3
cmd36 = on_command('欸嘿嘿',aliases={'嘿嘿'},priority=2)
@cmd36.handle()
async def cmd36_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\别老色迷迷的好不好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我刚刚刷抖音.mp3
cmd37 = on_command('你刚才再干什么',aliases={'你刚刚再干什么','你刚刚再干嘛'},priority=2)
@cmd37.handle()
async def cmd37_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我刚刚刷抖音.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#要亲亲抱抱举高高.mp3
cmd38 = on_command('要举高高吗',aliases={'要亲亲吗','要抱抱吗'},priority=2)
@cmd38.handle()
async def cmd38_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\要亲亲抱抱举高高.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#只有我一个人的呢.mp3
cmd39 = on_command('你一个人在家吗',aliases={'你一个人在家嘛','你爸妈在家吗'},priority=2)
@cmd39.handle()
async def cmd39_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\只有我一个人的呢.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#在的呢。小哥哥。.mp3
cmd40 = on_command('在吗',aliases={'在嘛'},priority=2)
@cmd40.handle()
async def cmd40_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\在的呢。小哥哥。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#没钱吃饭，你请我啊？.mp3
cmd41 = on_command('一起吃饭吗',aliases={'吃饭吗'},priority=2)
@cmd41.handle()
async def cmd41_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\没钱吃饭，你请我啊？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#主人，您在用我吗.mp3
cmd42 = on_command('召唤kaptree',priority=2)
@cmd42.handle()
async def cmd42_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\主人，您在用我吗.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#先说好 我不露脸.mp3
cmd43 = on_command('直播吗',priority=2)
@cmd43.handle()
async def cmd43_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\先说好 我不露脸.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你叫我不生气我就不生气啊 那多没面子。.mp3
cmd44 = on_command('别生气了',priority=2)
@cmd44.handle()
async def cmd44_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你叫我不生气我就不生气啊 那多没面子。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#为什么想骂我，小心我拉黑你.mp3
cmd45 = on_command('我想骂你',priority=2)
@cmd45.handle()
async def cmd45_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\为什么想骂我，小心我拉黑你.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我不是懒猪，我是世界上最勤快的小仙女。.mp3
cmd46 = on_command('小懒猪',aliases={'你好懒'},priority=2)
@cmd46.handle()
async def cmd46_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我不是懒猪，我是世界上最勤快的小仙女。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#以后你不要叫我宝贝，你要叫我爸爸.mp3
cmd47= on_command('宝贝',priority=2)
@cmd47.handle()
async def cmd47_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\以后你不要叫我宝贝，你要叫我爸爸.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不原谅.mp3
cmd48 = on_command('你原谅我了吗',aliases={'原谅我'},priority=2)
@cmd48.handle()
async def cmd48_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不原谅.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#今晚有事,改天吧.mp3
cmd49 = on_command('今晚约吗',aliases={'今晚吃个饭','今晚一起吃饭'},priority=2)
@cmd49.handle()
async def cmd49_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\今晚有事,改天吧.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你个大叔，怎么那么坏，老是要看这看那的.mp3
cmd50 = on_command('我想看看',aliases={'看看照片'},priority=2)
@cmd50.handle()
async def cmd50_(bot:Bot,event:Event):
    if int(event.get_user_id()) != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你个大叔，怎么那么坏，老是要看这看那的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )
