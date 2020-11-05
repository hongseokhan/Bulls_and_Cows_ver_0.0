import random

class Bot:
    
	def __init__(self,random_num_list = []):
		self._random_num_list = random_num_list

	def init_random_num_list(self):
		self.random_num_list = [str(x) for x in random.sample(range(0,10),4)]
	
		
	#property는 항상 setter 함수 위에 있어야함(순서중요!!)
	@property
	def random_num_list(self):
		return self._random_num_list	
	
	@random_num_list.setter
	def random_num_list(self,random_num_list):
		self._random_num_list = random_num_list