import redis

r=redis.Redis(host='localhost',port=6379)

r.mset({"India":"Delhi","Pakistan":"Karachi"})


if (r.exists("Syria")):
    print(r.get("Syria"))
else:
    print("Doesn't exist")