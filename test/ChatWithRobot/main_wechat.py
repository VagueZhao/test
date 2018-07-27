# tcp server
import socket;
import time;
import threading;
from JinkoRobot import *;
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from wxpy import *

chatbot = ChatBot("deepThought")
#bot = Bot(cache_path=True)
bot=Bot()
class trainer():
    def __init__(self, req, res):
        self.req = req
        self.res = res
    def training(self):
        chatbot.set_trainer(ListTrainer)
        chatbot.train([self.req,self.res,])

def getfriend():
    print(bot.friends())
    friends = bot.friends()
    # 获取群聊列表
    groups = bot.groups()
    print(friends)
    # 向好友发送消息
    #friend.send('我是机器人小糊涂，快跟我聊天吧！吼吼')

#应用程序入口类
class ApplicationServer:

	#构造函数初始化 socket
	def __init__(self, host="localhost", port=8005):
		self.connList = [];
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		self.socket.bind((host, port));
		self.socket.listen(100);
		print("你好, 我是S号的笨石头");
		print("");
		print("赶紧打开客户端和我聊天吧!");
		self.accept();

	#多线程接受用户请求
	def accept(self):
		while True:
			connection, address = self.socket.accept();
			# print('connect')
			thread = ChatThread(connection);
			thread.start();

#聊天线程
class ChatThread(threading.Thread):

	def __init__(self, conn):
		threading.Thread.__init__(self);

	def run(self):
		while True:
			try:
				recv = self.__connection.recv(8192);
			except:
				break;

			# print("收到:" + recv.decode('utf-8'))
			rebot = JinkoRobot();
			rebot.listenFor(recv.decode('utf-8'));
			answer = rebot.answer();
			# print('say:' + answer)
			self.__connection.send(answer.encode('utf-8'));

ApplicationServer();