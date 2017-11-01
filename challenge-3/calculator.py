#!/usr/bin/env python3
import sys
class Config(object):
    def __init__(self):
        args = sys.argv[1:]
        index = args.index('-c')
        self._config = {}
        with open(args[index+1]) as configfile:
            for i in configfile:
                (key,value) = i.strip().split('=')
                self._config[key.strip()] = value
    def get_config(self, key):
        return float(self._config[key])

class UserData(object):
    def __init__(self):    
        args = sys.argv[1:]
        index = args.index('-d')
        self._userdata = {} 
        with open(args[index+1]) as userdatafile:
            for i in userdatafile:
                (key,value) = i.strip().split(',')
                self._userdata[key] = value
    def get_userdata(self):
        return self._userdata

def dumptofile(s):
    args = sys.argv[1:]
    index = args.index('-o')
    with open(args[index+1], 'w') as outputfile:
        outputfile.write(s)

def f(salary):
    a = salary * 0.165
    b = salary - a - 3500
    c = salary - 3500
    if 0 >= c:
        return 0, salary - a          
    elif 0 < c <= 1500:
        return b * 0.03, salary - a - b * 0.03 - 0
    elif 1500 < c <= 4500:
        return b * 0.1 - 105, salary - a - (b * 0.1 - 105)
    elif 4500 < c <= 9000:
        return b * 0.2 - 555, salary - a - (b * 0.2 - 555)
    elif 9000 < c <= 35000:
        return b * 0.25 - 1005, salary - a - (b * 0.25 - 1005)
    elif 35000 < c <= 55000:
        return b * 0.3 - 2755, salary - a - (b * 0.3 - 2755)
    elif 55000 < c <= 80000:
        return b * 0.35 - 5505, salary - a - (b * 0.35 - 5505)
    else:
        return b * 0.45 - 13505, salary - a - (b * 0.45 - 13505)
if __name__ == '__main__':
    config = Config()
    userdata = UserData()
    for key,value in userdata.get_userdata().items():
        x = float(value)
        k = int(key) 
        h = config.get_config('JiShuH')
        l = config.get_config('JiShuL')
        if x > config.get_config('JiShuH'):
            print(k,int(x),'{:.2f}'.format(h * 0.165),'{:.2f}'.format((h - h * 0.165 - 3500) * 0.25 - 1005),'{:.2f}'.format(f(h)),sep=',')
        elif x < config.get_config('JiShuL'):
            print(k,int(x),'{:.2f}'.format(l * 0.165),0.00,'{:.2f}'.format(f(l)),sep=',')
        else:
            print(k,int(x),'{:.2f}'.format(x * 0.165),'{:.2f}'.format(f(x)[0]),'{:.2f}'.format(f(x)[1]),sep=',')
