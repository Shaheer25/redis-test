import redis

r=redis.Redis(host='localhost',port=6379)

r.set("India",'Delhi')
r.set("Pakistan",'Karachi')

print(r.get("India"))