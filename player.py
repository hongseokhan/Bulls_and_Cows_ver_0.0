class Player:
    
    def __init__(self,input_num_list = []):
        self._input_num_list = input_num_list
    
    def input_rule(self,input_num_list):
        
        flag = True
        message = []
    
        if not(input_num_list.isdecimal()):
            flag = False
            message = f'{input_num_list}는 숫자가 아닙니다.'

        elif len(input_num_list) != 4:
            flag = False
            message = f'{input_num_list}는 4자리 숫자가 아닙니다.'
        
        elif len(input_num_list) != len(set(input_num_list)):
            flag = False
            message = f'{input_num_list}는 중복된 숫자가 존재 합니다'
        return flag, message
    def check_input_num_list(self):
        
        flag = False
        
        while flag is False:
            input_num_list = input('4자리 숫자를 입력하세요:')
        
            flag, message = self.input_rule(input_num_list)
            if flag is False:
                print(message)
        self._input_num_list = input_num_list
    @property
    def input_num_list(self):
        return self._input_num_list
    
    @input_num_list.setter
    def input_num_list(self,input_num_list):
        self._input_num_list = input_num_list
    

