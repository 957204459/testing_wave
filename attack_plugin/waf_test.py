# coding: utf-8
'''
Created on Dec 30, 2019

@author: guimaizi
'''
import config_function,http_testing
class waf_test:
    def __init__(self):
        self.config=config_function.config_function()
        self.http_testing=http_testing.http_testing()
    def dict_waf(self,data):
        for i in ['501page.html','501 Not Implemented','501 by TSW']:
            if i in data:
                return False
        return True
    def run(self):
        data=self.config.callback_target()
        data['url']=data['url']+'<img src=a onerror=alert()>'
        '''if '501page.html' in self.http_testing.callback_response(data) or '501 Not Implemented' in self.http_testing.callback_response(data) or '501 by TSW' in self.http_testing.callback_response(data):
            print('have waf...')
            return 0'''
        if self.dict_waf(self.http_testing.callback_response(data))==False:
            print('have waf...')
            return 0
            
if __name__ == '__main__':
    p1=waf_test()
    p1.run()
        