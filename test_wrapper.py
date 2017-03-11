#-*- coding:utf-8 -*-

import requests

class exception_track:
    val = None
    def safe_get(text):
        def decorator(func):
            def wrapper(*args, **kw):
                #print '%s %s():' % (text, func.__name__)
                #list(args)[-1] = 456
                #print tuple(args),kw,list(args)[-1]
                print dir(func)
                #html = kw.get('http://www.baidu.com')
                #print html.status_code
                #html = args[-1].get()
                
                return func(*args, **kw)
            return wrapper
        return decorator    
    
    @safe_get(val)
    def now(self,val,val2):
        #print "hello"
        return val

#str = 'hello'  
#try:  
    ##x = 10/0  
    #assert len(str) == 3  
#except AssertionError,x:  
    #print 'assert error',x 

res = requests.session()
#res = exception_track()
#print res.now("abc",res)
try:
    html = res.get('http://www.juzimi.com')
    assert False
    #raise Exception('123')


except requests.exceptions.InvalidURL:
    print 'httperror'
#except Exception as e:
    #print 'exc',e
except AssertionError:
    print 'here'
