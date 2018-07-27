from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# 初始化机器人
chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 这里先使用该库现成的中文语料库训练
chatbot.train("chatterbot.corpus.chinese")
# 这里进行简单测试
while True:
 speak = input("S号的小石头:\n")
 print("真真:")
 print(chatbot.get_response(speak))
