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
    def get_config(self):
        
class UserData(object):
    def __init__(self):    
        args = sys.argv[1:]
        index = args.index('-d')
        self._userdata = {} 
        with open(args[index+1]) as userdatafile:
            for i in userdatafile:
                (key,value) = i.strip().split(',')
                self._userdata[key] = value
if __name__ == '__main__':
    config = Config()
    userdata = UserData()
    print(config.get_config('JiShuH'))
