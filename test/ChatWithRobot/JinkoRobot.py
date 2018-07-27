#笨石头
import json;
import urllib.request;
import urllib.parse;

class JinkoRobot:
	
	__answer = '';

	def __init__(self):
		pass;

	#倾听话语
	def listenFor(self, string):
		self.__answer = self.thinking(string);

	# 思考着
	def thinking(self, string):
		says = urllib.parse.quote_plus(string);
		f = urllib.request.urlopen("http://www.tuling123.com/openapi/api?key=4bc32d41c10be18627438ae45eb839ac&info=" + says);
		json_str = f.read();
		thinkdata = json.loads(json_str.decode('utf-8'));
		f.close();
		
		if(thinkdata['code'] > 40000 and thinkdata['code'] < 40010):
			return "今天被你问得有点累了, 过会再问吧!";
		return thinkdata['text'];

	#和你交流回答
	def answer(self):
		return self.__answer;