from bot import Bot
from player import Player



class Gameinterface:
    def __init__(self):
        self._score_strikes = 25
        self._score_balls = 10
        self._score_nothing = 0
        self._score_try = 100
        self._try_max =10
        self._score = 1000
        self._trys = 1
        self._game_score = 0
        self._answer_num_list = []
        self._strikes = 0
        self._balls = 0
    def sb_count_calculator(self,answer_num_list,input_num_list):
        for n,nvalue in enumerate(answer_num_list):    
            for m,mvalue in enumerate(input_num_list):
                if nvalue == mvalue:
                    if n == m:
                        self._strikes += 1
                    else:
                        self._balls += 1
                        
    def score_calculator(self,strikes,balls):
        self._score -= self._score_try
        
        if strikes == 0 and balls == 0:
            self._score += self._score_nothing
        
        else:
            self._score += strikes * self._score_strikes  + balls * self._score_balls
            
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        self._score = score
    
    @property
    def strike(self):
        return self._strikes

    @strike.setter
    def strike(self, strikes):
        self._strikes = strikes
	
    @property
    def ball(self):
        return self._balls

    @ball.setter
    def ball(self, balls):
        self._balls = balls

    def show_result(self,strikes,balls,trys,score):
        if strikes ==0 and balls == 0:
            print(f'<{trys}차 시도>, Nothing 입니다.')
            print(f'{score}점')
            print('-----------------------------------------------')
        
        else:
            print(f'<{trys}차시도> {strikes}스트라이크{balls}볼 입니다.')
            print(f'{score}점')
            print('-----------------------------------------------')
    def win_game(self,trys,score):
        print('\n축하합니다\n')
        print(f'{trys}회 시도만에 성공 했습니다\n')
        print(f'당신의 점수는 {score}점 입니다.')
    
    def lose_game(self,try_max,score,random_num_list):
        print('\n아쉽습니다')
        print(f'{try_max}회 시도만에 성공하지 못했습니다')
        print(f'당신의 점수는 {score}점 입니다.')
        print(f'봇이 가지고 있는 숫자는 {random_num_list}입니다')

    def make_bot(self):
        bot = Bot()
        bot.init_random_num_list()
        bot_num = bot.random_num_list
        return bot_num
    
    def start_game(self):
        bot_num = self.make_bot()
        while True:
            player = Player()
            player.check_input_num_list()
            player_num = player.input_num_list
            self.sb_count_calculator(bot_num,player_num)
            strikes_num = self.strike
            balls_num = self.ball
            self.score_calculator(strikes_num,balls_num)
            self._game_score = self.score

            self.show_result(strikes_num,balls_num,self._trys,self._game_score)
            
            if self._strikes == 4:
                self.win_game(self._trys,self._game_score)
                break
            
            elif self._trys >= self._try_max or self._game_score <= 0:
                self.lose_game(self._try_max,self._game_score,bot_num)
                break
            self._trys += 1
