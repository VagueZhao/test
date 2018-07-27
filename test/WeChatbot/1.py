from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from wxpy import *


# 初始化机器人
chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 这里先使用该库现成的中文语料库训练
chatbot.train("chatterbot.corpus.chinese")
# 使用英文语料库训练它
#chatbot.train("chatterbot.corpus.english")


# 初始化机器人，这里会生成一张二维码，用微信扫码继续登录
#微信机器人登录有3种模式，
#(1)极简模式:robot = Bot()
#(2)终端模式:robot = Bot(console_qr=True)
#(3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
bot = Bot(cache_path=True)# 用于接入微信的机器人

# 向文件传输助手发送消息
#bot.file_helper.send('Hello from wxpy!')

# 获取好友列表，这里随意使用一个好友进行测试
print(bot.friends())
friend = bot.friends().search()[1]
print(friend)

# 获取群聊列表
wxpy_groups = bot.groups().search('幸福之家！')[0]
print(wxpy_groups)

# 向好友发送消息
wxpy_groups.send('hi')

# 使用机器人进行自动回复
@bot.register(wxpy_groups)
def reply_my_friend(msg):
    return chatbot.get_response(msg.text).text
embed()

