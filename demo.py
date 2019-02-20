import smartninja_redis as redis
from smartninja_redis import Redis

# from_url()
r_url = redis.from_url(url="localhost")

r_url.set(name="Ninja", value="Smart")

print(r_url.get("Ninja"))

# Redis class
r_class = Redis(host="localhost")

r_class.set(name="smart", value="ninja")

print(r_class.get("smart"))
