import time

import redis

r=redis.Redis(host='localhost',port=6379)

r.psetex("Pakistan",1000,"Karachi")#only stores upto 1ms = 1sec

print(r.get("Pakistan"))

time.sleep(2) # It will not print because of psetex

print(r.get("Pakistan"))
