from bot import Gamebot
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
        
    def show_result(self,strikes,balls,trys,score):
        if strikes ==0 and balls == 0:
            print(f'<{trys}차 시도>, Nothing 입니다.')
            print(f'{score}점')
            print('-----------------------------------------------')
        
        else:
            print(f'<{trys}차시도> {strikes}스트라이크 {balls}볼 입니다.')
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
        game = Gamebot()
        game.init_random_num_list()
        bot = game.random_num_list
        return bot
    
    def start_game(self):
        bot = self.make_bot()
        while True:
            game = Gamebot()
            player_num = Player()
            player_num.check_input_num_list()
            player = player_num.input_num_list
            game.sb_count_calculator(bot,player)
            strike_num = game.strikes
            ball_num = game.balls
            self.score_calculator(strike_num,ball_num)
            self._game_score = self.score
            self.show_result(game.strikes,game.balls,self._trys,self._game_score)
            
            if strike_num == 4:
                self.win_game(self._trys,self._game_score)
                break
            
            elif self._trys >= self._try_max or self._game_score <= 0:
                self.lose_game(self._try_max,self._game_score,bot)
                break
            self._trys += 1
            