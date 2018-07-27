import json;
import urllib.request;
import urllib.parse;
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from wxpy import *

chatbot = ChatBot("deepThought")
bot = Bot(cache_path=True)
#bot=Bot()
class trainer():
    def __init__(self, req, res):
        self.req = req
        self.res = res
    def training(self):
        chatbot.set_trainer(ListTrainer)
        chatbot.train([self.req,self.res,])

#图灵机器人类
class JinkoRobot:
    __answer = '';

    def __init__(self):
        pass;

    # 倾听话语
    def listenFor(self, string):
        self.__answer = self.thinking(string);

    # 思考着
    def thinking(self, string):
        says = urllib.parse.quote_plus(string);
        f = urllib.request.urlopen(
            "http://www.tuling123.com/openapi/api?key=4bc32d41c10be18627438ae45eb839ac&info=" + says);
        json_str = f.read();
        thinkdata = json.loads(json_str.decode('utf-8'));
        f.close();

        if (thinkdata['code'] > 40000 and thinkdata['code'] < 40010):
            return "今天被你问得有点累了, 过会再问吧!";
        return thinkdata['text'];

    # 和你交流回答
    def answer(self):
        return self.__answer;

def getfriend():
    print(bot.friends())
    #friend = bot.friends().search("大白菜")[0]
    # 获取群聊列表
    friend = bot.groups().search('糊涂涂')[0]
    print(friend)
    # 向好友发送消息
    #friend.send('我是机器人小糊涂，快跟我聊天吧！吼吼')

    # 文本
    # TEXT = 'Text'
    # 位置
    # MAP = 'Map'
    # 名片
    # CARD = 'Card'
    # 提示
    # NOTE = 'Note'
    # 分享
    # SHARING = 'Sharing'
    # 图片
    # PICTURE = 'Picture'
    # 语音
    # RECORDING = 'Recording'
    # 文件
    # ATTACHMENT = 'Attachment'
    # 视频
    # VIDEO = 'Video'
    # 好友请求
    # FRIENDS = 'Friends'
    # 系统
    # SYSTEM = 'System'

    # 发送图片
    # friend.send_image('my_picture.png')
    # 发送视频
    # friend.send_video('my_video.mov')
    # 发送文件
    # friend.send_file('my_file.zip')
    # 以动态的方式发送图片

    # 使用图灵机器人进行自动回复
    @bot.register(friend)
    def reply_my_friend(msg):
        print(msg.type)
        #if msg.text:
        rebot = JinkoRobot();
        rebot.listenFor(msg.text);
        print(rebot.answer())
        return rebot.answer()
        #elif msg.type== 'Picture':
            #friend.send_image('./img/2.png')
        #elif msg.type == 'Recording':
           # friend.send('你的声音可真好听！')
        #elif msg.type == 'Video':
           # friend.send_image('./img/2.png')
    embed()
getfriend()

