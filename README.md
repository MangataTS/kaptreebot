# kaptreebot机器人开源

## 关于项目

本项目基于[nonebot2]( https://v2.nonebot.dev/)框架，采用[go-cqhttp]( https://github.com/Mrs4s/go-cqhttp)协议，python3语言编写的

## 关于配置
如果你是一个纯小白，那么请先下载[python3]( https://www.python.org/)，记得勾选环境变量的选项
如果你已经配置好python环境，那么请安装nonebot2 -> 打开你的cmd，

然后输入`pip install nonebot2`

接着输入`pip install requests`

接着输入`pip install aiocqhttp`

接着输入`pip install requests_html`
后续就更具你的需求自己安装库啦

## 使用说明
1.请先配置好go-cqhttp协议(只用修改我文件夹的config.hjson文件里面)，当然这个我这里配置好了的，你只需要更改QQ的UIN(账号)和password(密码)即可
&nbsp;

2.在py编译器打开kaptreebot文件夹，然后运行bot.py文件

&nbsp;
如果没有py编译器的话，为了你运行方便，我写了个begin.bat，双击它也能运行(当然无论哪种方式你都要有py环境)

3.在我的kaptreebot目录下面有两个文件.env.dev和.env.prod，请在里面修改成你的QQ号

## 目前实现功能
|功能                   |使用方法
--|--
|1.每日一句             |eg:每日一句
|2.天气查询             |eg:天气 成都
|3.单词翻译             |eg:翻译 cat
|4.戳一戳               |eg:手机戳我头像
|5.每日一图             |eg:每日一图/setu/来一份色图/mc酱
|6.我要抱抱             |eg:我要抱抱/我要亲亲
|7.新年快乐             |eg:新年快乐(关键词匹配)
|8.情感语录 && 毒鸡汤    |eg:情感语录/毒鸡汤/舔狗日记 (关键词匹配)
|9.社会语录             |eg:社会语录(关键词匹配)
|10.To be continue……   |

## 关于作者
作者: Mangata
QQ:1196991321
作者的交流群: [传送门]( https://jq.qq.com/?_wv=1027&k=UwKSTvSn)
作者的博客 [传送门]( https://www.cnblogs.com/Mangata/)

## 感谢人员
感谢对我指导的群友，还感谢群里帮我测试的同学@zoey,@Untergehen

快来star我吧

后续有时间的话，我会更新的(可能跟新的周期有点长 To Be Continue……

&nbsp;
&nbsp;
&nbsp;

## 更新
### 版本 0.4  &nbsp;&nbsp;&nbsp;&nbsp;-2021.2.23
1.修复了bot自己调用自己的bug

2.新增了50条，部分关键词，部分命令的语音发送(注意:私聊的时候手机端收不到语音消息，电脑端能收到，群聊的时候都能看到，这个bug应该是go-cqhttp的作者写出了bug)

3.更新了go-cqhttp的版本


### 版本 0.3 &nbsp;&nbsp;&nbsp;&nbsp;-2021.2.22
1.更新了语音发送(但是这个mp3文件云盘还未找到，实在找不到，到时候自己写一个了)

2.将代码的priority全部重新编写

3.添加了图灵机器人API,让bot聊天更加智能，但是每天只能使用100次(后面会转腾讯/百度)


### 版本 0.2 &nbsp;&nbsp;&nbsp;&nbsp;-2021.2.18
1.更新了爬虫 舔狗日记/毒鸡汤/社会语录

2.将许多命令都改成了关键词匹配 eg: 每日一图、情感语录、mc酱等等

3.添加了 @群红包最后一位领取的成员

4.更新了群消息撤回后发送调戏消息

5.更新了好友添加自动同意功能

6.更新了文档信息(关于小白配置自己的机器人)
