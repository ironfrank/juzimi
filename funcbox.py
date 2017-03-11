#-*- coding:utf-8 -*-
import time
import hashlib, random

def create_id():
    timestamp = time.time()
    timestamp = '%f'%timestamp
    timestamp = ''.join(timestamp.split('.'))
    
    random_number = random.uniform(1000,9999)
    random_number = '%.6f'%random_number
    random_number = ''.join(random_number.split('.'))
    return timestamp + random_number

def create_md5(src):
    md = hashlib.md5()
    md.update(src)
    return md.hexdigest()
