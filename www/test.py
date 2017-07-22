import orm
from models import User, Blog, Comment
import asyncio, logging
import aiomysql

def test(loop):
    yield from orm.create_pool(loop,user='root', password='', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()

for x in test(loop):
    pass