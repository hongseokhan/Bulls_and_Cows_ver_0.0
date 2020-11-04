import random

class Gamebot:
    
	def __init__(self,random_num_list = [],strikes = 0,balls = 0):
		self._random_num_list = random_num_list
		self._strikes = strikes
		self._balls = balls

	def init_random_num_list(self):
		self.random_num_list = [str(x) for x in random.sample(range(0,10),4)]
	
	def sb_count_calculator(self,random_num_list,input_num_list):
		

		for n,nvalue in enumerate(random_num_list):
			for m,mvalue in enumerate(input_num_list):
				if nvalue == mvalue:
					if n == m:
						self._strikes += 1
					else:
						self._balls +=1
		
	#property는 항상 setter 함수 위에 있어야함(순서중요!!)
	@property
	def random_num_list(self):
		return self._random_num_list	
	
	@random_num_list.setter
	def random_num_list(self,random_num_list):
		self._random_num_list = random_num_list

	@property
	def strikes(self):
		return self._strikes

	@strikes.setter
	def strikes(self, strikes):
		self._strikes = strikes
	@property
	def balls(self):
		return self._balls

	@balls.setter
	def balls(self, balls):
		self._balls = balls
