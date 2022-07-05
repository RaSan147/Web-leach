from config import config
from y import push, get

config.x = 1
push(config)
print(config.x)

config.x = 3
get()