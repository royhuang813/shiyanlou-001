#!/usr/bin/env python3
import sys
class Config():
    def __init__(self):
        args = sys.argv[1:]
        index = args.index('-c')
        self._config = {}
        with open(args[index+1]) as configfile:
            for i in configfile:
                (key,value) = i.strip().split('=')
                self._config[key.strip()] = value
    def get_config(self):
        print(self._config)
    def calculator(self):
        pass
class UserData(Config):
    def __init__(self):    
        args = sys.argv[1:]
        index = args.index('-d')
        self._userdata = {} 
        with open(args[index+1]) as userdatafile:
            for i in userdatafile:
                (key,value) = i.strip().split(',')
                self._userdata[key] = value
                return values
    def calculator(self):
        values = salary
        a = salary * 0.165             #Social_insurance 
        b = salary - a - 3500              #Taxable_income 
        c = salary - 3500                  #Tax_threshold 
        if 0 >= c:
            salary - a          #result: After_tax_salary
        elif 0 < c <= 1500:
            return salary - a - b * 0.03 - 0    
        elif 1500 < c <= 4500:
            return salary - a - (b * 0.1 - 105)
        elif 4500 < c <= 9000:
            return salary - a - (b * 0.2 - 555)
        elif 9000 < c <= 35000:
            return salary - a - (b * 0.25 - 1005)
        elif 35000 < c <= 55000:
            return salary - a - (b * 0.3 - 2755)
        elif 55000 < c <= 80000:
            return salary - a - (b * 0.35 - 5505)
        else:
            return salary - a - (b * 0.45 - 13505)
   
if __name__ == '__main__':
    config = Config()
    userdata = UserData()
    config.get_config()
    userdata.calculator()
