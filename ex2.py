import redis

r=redis.Redis(host='localhost',port=6379)

r.mset({"India":"Delhi","Pakistan":"Karachi"})


print(r.get("Pakistan"))